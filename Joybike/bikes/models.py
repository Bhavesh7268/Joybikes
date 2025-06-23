
# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

class Bike(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    primary_color = models.CharField(max_length=7, default='#e40521')
    secondary_color = models.CharField(max_length=7, default='#1a1a1a')
    
    # Images
    hero_image = models.ImageField(upload_to='bikes/')
    features_image = models.ImageField(upload_to='bikes/')
    design_image = models.ImageField(upload_to='bikes/')
    engine_image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    
    # Features
    features_title = models.CharField(max_length=200, blank=True)
    features_description = models.TextField()
    design_title = models.CharField(max_length=200, blank=True)
    design_description = models.TextField()
    
    # Engine specs
    engine_type = models.CharField(max_length=200)
    displacement = models.CharField(max_length=50)
    bore_stroke = models.CharField(max_length=50)
    compression_ratio = models.CharField(max_length=50)
    max_power = models.CharField(max_length=50)
    max_torque = models.CharField(max_length=50)
    fuel_system = models.CharField(max_length=100)
    fuel_tank_capacity = models.CharField(max_length=50)
    
    # [Add all other specification fields as before]
    clutch_type = models.CharField(max_length=100, default='Wet, multiplate clutch')
    transmission_type = models.CharField(max_length=50, default='6-speed')
    transmission_image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    
    # Chassis & Brakes Fields
    frame_type = models.CharField(max_length=100, default='Diamond')
    front_suspension = models.CharField(max_length=200, default='Showa 41 mm SFF-BP USD fork')
    rear_suspension = models.CharField(max_length=200, default='Monoshock damper, 10-step preload adjustable')
    front_brake = models.CharField(max_length=200, default='310 mm dual disc with 2-piston calipers, ABS')
    rear_brake = models.CharField(max_length=200, default='240 mm single disc with single-piston caliper, ABS')
    front_tyre = models.CharField(max_length=100, default='120/70ZR17M/C (58W)')
    rear_tyre = models.CharField(max_length=100, default='180/55ZR17M/C (73W)')
    chassis_image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    
    # Dimensions Fields
    dimensions = models.CharField(max_length=200, default='2,110 mm × 750 mm × 1,150 mm')
    wheelbase = models.CharField(max_length=50, default='1,450 mm')
    ground_clearance = models.CharField(max_length=50, default='130 mm')
    seat_height = models.CharField(max_length=50, default='810 mm')
    kerb_weight = models.CharField(max_length=50, default='207 kg')
    dimensions_image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class BikeImage(models.Model):
    bike = models.ForeignKey(Bike, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bikes/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.bike.name} - {self.caption or 'Image'}"