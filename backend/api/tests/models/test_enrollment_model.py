from django.test import TestCase 
from django.db import models 
from django.utils import timezone
from api.models import Enrollment, Members, Manager, Sector, Journey
import uuid


class TestEnrollmentModel(TestCase):
  def setUp(self) -> None:
    """Cria dados de teste para cada teste"""
    self.manager = Manager.objects.create_user(
      email="manager@test.com",
      password="test123",
      first_name="John",
      last_name="Manager"
    )
    
    self.member = Members.objects.create_user(
      email="member@test.com",
      password="test123",
      first_name="Jane",
      last_name="Member"
    )
    
    self.sector = Sector.objects.create(
      search_code="SEC001",
      name="Engineering",
      description="Engineering sector"
    )
    
    self.journey = Journey.objects.create(
      name="Python Developer Journey",
      description="Journey for Python developers",
      sector=self.sector
    )
    
    self.enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager,
      journey=self.journey,
      sector=self.sector
    )
  
  def test_if_can_import_model_class_in_module(self) -> None:
    """Testa se é possível importar o modelo Enrollment"""
    try: 
      from api.models import Enrollment
    except ImportError:
      raise ImportError("Was not possible to import the enrollment model")
    
  def test_if_enrollment_model_have_correct_superclass(self) -> None:
    """Testa se Enrollment herda corretamente de models.Model"""
    try:
      from api.models import Enrollment
      self.assertTrue(issubclass(Enrollment, models.Model))

    except ImportError:
      raise ImportError("Was not possible to import the enrollment model")
    
  def test_if_enrollment_model_have_correct_fields(self) -> None:
    """Testa se o modelo possui todos os campos esperados"""
    expected_fields = ['id', 'member', 'manager', 'created_at', 'updated_at', 'journey', 'sector']
    model_fields = [field.name for field in Enrollment._meta.get_fields()]
    
    for field in expected_fields:
      self.assertIn(field, model_fields, f"Field '{field}' not found in Enrollment model")
  
  def test_enrollment_id_field_is_uuid(self) -> None:
    """Testa se o campo id é um UUID"""
    id_field = Enrollment._meta.get_field('id')
    self.assertIsInstance(id_field, models.UUIDField)
    self.assertTrue(id_field.primary_key)
  
  def test_enrollment_member_field_is_foreign_key(self) -> None:
    """Testa se o campo member é uma ForeignKey para Members"""
    member_field = Enrollment._meta.get_field('member')
    self.assertIsInstance(member_field, models.ForeignKey)
    self.assertEqual(member_field.related_model, Members)
    self.assertEqual(member_field.remote_field.on_delete, models.CASCADE)
  
  def test_enrollment_manager_field_is_foreign_key(self) -> None:
    """Testa se o campo manager é uma ForeignKey para Manager"""
    manager_field = Enrollment._meta.get_field('manager')
    self.assertIsInstance(manager_field, models.ForeignKey)
    self.assertEqual(manager_field.related_model, Manager)
    self.assertEqual(manager_field.remote_field.on_delete, models.SET_NULL)
    self.assertTrue(manager_field.null)
    self.assertTrue(manager_field.blank)
  
  def test_enrollment_journey_field_is_foreign_key(self) -> None:
    """Testa se o campo journey é uma ForeignKey para Journey"""
    journey_field = Enrollment._meta.get_field('journey')
    self.assertIsInstance(journey_field, models.ForeignKey)
    self.assertEqual(journey_field.related_model, Journey)
    self.assertEqual(journey_field.remote_field.on_delete, models.SET_NULL)
    self.assertTrue(journey_field.null)
    self.assertTrue(journey_field.blank)
  
  def test_enrollment_sector_field_is_foreign_key(self) -> None:
    """Testa se o campo sector é uma ForeignKey para Sector"""
    sector_field = Enrollment._meta.get_field('sector')
    self.assertIsInstance(sector_field, models.ForeignKey)
    self.assertEqual(sector_field.related_model, Sector)
    self.assertEqual(sector_field.remote_field.on_delete, models.SET_NULL)
    self.assertTrue(sector_field.null)
    self.assertTrue(sector_field.blank)
  
  def test_enrollment_created_at_field(self) -> None:
    """Testa se o campo created_at é um DateTimeField com auto_now_add"""
    created_at_field = Enrollment._meta.get_field('created_at')
    self.assertIsInstance(created_at_field, models.DateTimeField)
    self.assertTrue(created_at_field.auto_now_add)
  
  def test_enrollment_updated_at_field(self) -> None:
    """Testa se o campo updated_at é um DateTimeField com auto_now"""
    updated_at_field = Enrollment._meta.get_field('updated_at')
    self.assertIsInstance(updated_at_field, models.DateTimeField)
    self.assertTrue(updated_at_field.auto_now)
  
  def test_can_create_enrollment(self) -> None:
    """Testa se é possível criar um enrollment"""
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager,
      journey=self.journey,
      sector=self.sector
    )
    
    self.assertIsNotNone(enrollment.id)
    self.assertEqual(enrollment.member, self.member)
    self.assertEqual(enrollment.manager, self.manager)
    self.assertEqual(enrollment.journey, self.journey)
    self.assertEqual(enrollment.sector, self.sector)
  
  def test_can_create_enrollment_without_manager(self) -> None:
    """Testa se é possível criar um enrollment sem manager"""
    enrollment = Enrollment.objects.create(
      member=self.member,
      journey=self.journey,
      sector=self.sector
    )
    
    self.assertIsNotNone(enrollment.id)
    self.assertEqual(enrollment.member, self.member)
    self.assertIsNone(enrollment.manager)
  
  def test_can_create_enrollment_without_journey(self) -> None:
    """Testa se é possível criar um enrollment sem journey"""
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager,
      sector=self.sector
    )
    
    self.assertIsNotNone(enrollment.id)
    self.assertIsNone(enrollment.journey)
  
  def test_can_create_enrollment_without_sector(self) -> None:
    """Testa se é possível criar um enrollment sem sector"""
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager,
      journey=self.journey
    )
    
    self.assertIsNotNone(enrollment.id)
    self.assertIsNone(enrollment.sector)
  
  def test_member_is_required(self) -> None:
    """Testa que o campo member é obrigatório"""
    from django.db import IntegrityError
    
    with self.assertRaises(IntegrityError):
      Enrollment.objects.create(
        manager=self.manager,
        journey=self.journey,
        sector=self.sector
      )
  
  def test_enrollment_created_at_is_automatically_set(self) -> None:
    """Testa se created_at é automaticamente definido"""
    before = timezone.now()
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager
    )
    after = timezone.now()
    
    self.assertIsNotNone(enrollment.created_at)
    self.assertGreaterEqual(enrollment.created_at, before)
    self.assertLessEqual(enrollment.created_at, after)
  
  def test_enrollment_updated_at_is_automatically_set(self) -> None:
    """Testa se updated_at é automaticamente definido"""
    before = timezone.now()
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager
    )
    after = timezone.now()
    
    self.assertIsNotNone(enrollment.updated_at)
    self.assertGreaterEqual(enrollment.updated_at, before)
    self.assertLessEqual(enrollment.updated_at, after)
  
  def test_enrollment_updated_at_changes_on_update(self) -> None:
    """Testa se updated_at muda ao atualizar o enrollment"""
    enrollment = Enrollment.objects.create(
      member=self.member,
      manager=self.manager
    )
    
    original_updated_at = enrollment.updated_at
    
    # Aguarda um pouco para garantir que o timestamp seja diferente
    import time
    time.sleep(0.01)
    
    enrollment.manager = None
    enrollment.save()
    
    enrollment.refresh_from_db()
    self.assertGreater(enrollment.updated_at, original_updated_at)
  
  def test_enrollment_cascade_delete_member(self) -> None:
    """Testa se deletar um member deleta seus enrollments (CASCADE)"""
    enrollment_id = self.enrollment.id
    
    # Verifica se o enrollment existe
    self.assertTrue(Enrollment.objects.filter(id=enrollment_id).exists())
    
    # Deleta o member
    self.member.delete()
    
    # Verifica se o enrollment foi deletado
    self.assertFalse(Enrollment.objects.filter(id=enrollment_id).exists())
  
  def test_enrollment_set_null_delete_manager(self) -> None:
    """Testa se deletar um manager seta manager como NULL (SET_NULL)"""
    enrollment_id = self.enrollment.id
    manager_id = self.manager.id
    
    # Verifica que o manager está setado
    self.assertEqual(self.enrollment.manager.id, manager_id)
    
    # Deleta o manager
    self.manager.delete()
    
    # Busca o enrollment novamente
    enrollment = Enrollment.objects.get(id=enrollment_id)
    
    # Verifica se manager é NULL
    self.assertIsNone(enrollment.manager)
  
  def test_enrollment_set_null_delete_journey(self) -> None:
    """Testa se deletar uma journey seta journey como NULL (SET_NULL)"""
    enrollment_id = self.enrollment.id
    journey_id = self.journey.id
    
    # Verifica que a journey está setada
    self.assertEqual(self.enrollment.journey.id, journey_id)
    
    # Deleta a journey
    self.journey.delete()
    
    # Busca o enrollment novamente
    enrollment = Enrollment.objects.get(id=enrollment_id)
    
    # Verifica se journey é NULL
    self.assertIsNone(enrollment.journey)
  
  def test_enrollment_set_null_delete_sector(self) -> None:
    """Testa se deletar um sector seta sector como NULL (SET_NULL)"""
    enrollment_id = self.enrollment.id
    sector_id = self.sector.id
    
    # Verifica que o sector está setado
    self.assertEqual(self.enrollment.sector.id, sector_id)
    
    # Deleta o sector
    self.sector.delete()
    
    # Busca o enrollment novamente
    enrollment = Enrollment.objects.get(id=enrollment_id)
    
    # Verifica se sector é NULL
    self.assertIsNone(enrollment.sector)
  
  def test_can_retrieve_enrollment_by_id(self) -> None:
    """Testa se é possível recuperar um enrollment pelo ID"""
    retrieved_enrollment = Enrollment.objects.get(id=self.enrollment.id)
    self.assertEqual(retrieved_enrollment, self.enrollment)
  
  def test_can_retrieve_enrollments_by_member(self) -> None:
    """Testa se é possível recuperar enrollments de um membro específico"""
    enrollments = Enrollment.objects.filter(member=self.member)
    self.assertIn(self.enrollment, enrollments)
  
  def test_can_retrieve_enrollments_by_manager(self) -> None:
    """Testa se é possível recuperar enrollments de um manager específico"""
    enrollments = Enrollment.objects.filter(manager=self.manager)
    self.assertIn(self.enrollment, enrollments)
  
  def test_can_retrieve_enrollments_by_journey(self) -> None:
    """Testa se é possível recuperar enrollments de uma journey específica"""
    enrollments = Enrollment.objects.filter(journey=self.journey)
    self.assertIn(self.enrollment, enrollments)
  
  def test_can_retrieve_enrollments_by_sector(self) -> None:
    """Testa se é possível recuperar enrollments de um sector específico"""
    enrollments = Enrollment.objects.filter(sector=self.sector)
    self.assertIn(self.enrollment, enrollments)
  
  def test_can_update_enrollment(self) -> None:
    """Testa se é possível atualizar um enrollment"""
    new_manager = Manager.objects.create_user(
      email="new_manager@test.com",
      password="test123",
      first_name="New",
      last_name="Manager"
    )
    
    self.enrollment.manager = new_manager
    self.enrollment.save()
    
    self.enrollment.refresh_from_db()
    self.assertEqual(self.enrollment.manager, new_manager)
  
  def test_can_delete_enrollment(self) -> None:
    """Testa se é possível deletar um enrollment"""
    enrollment_id = self.enrollment.id
    self.enrollment.delete()
    
    self.assertFalse(Enrollment.objects.filter(id=enrollment_id).exists())
  
  def test_enrollment_has_correct_string_representation(self) -> None:
    """Testa a representação em string do enrollment (se __str__ estiver implementado)"""
    # Se não houver __str__ implementado, este teste verifica o comportamento padrão
    str_repr = str(self.enrollment)
    self.assertIsNotNone(str_repr)
  
  def test_multiple_enrollments_same_member(self) -> None:
    """Testa se um member pode ter múltiplos enrollments"""
    journey2 = Journey.objects.create(
      name="Database Design Journey",
      description="Journey for database design",
      sector=self.sector
    )
    
    enrollment2 = Enrollment.objects.create(
      member=self.member,
      manager=self.manager,
      journey=journey2,
      sector=self.sector
    )
    
    member_enrollments = Enrollment.objects.filter(member=self.member)
    self.assertEqual(member_enrollments.count(), 2)
    self.assertIn(self.enrollment, member_enrollments)
    self.assertIn(enrollment2, member_enrollments)
  
  def test_enrollment_id_is_unique(self) -> None:
    """Testa se cada enrollment tem um ID único"""
    enrollment2 = Enrollment.objects.create(
      member=self.member,
      manager=self.manager
    )
    
    self.assertNotEqual(self.enrollment.id, enrollment2.id)
  
  def test_enrollment_id_is_uuid_format(self) -> None:
    """Testa se o ID do enrollment é um UUID válido"""
    self.assertIsInstance(self.enrollment.id, uuid.UUID)