# 
from django.contrib import admin
from .models import Bike, BikeImage

class BikeImageInline(admin.TabularInline):
    model = BikeImage
    extra = 3

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    inlines = [BikeImageInline]  # Add this line to include the carousel
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['name', 'title', 'description', 'price',
                      'primary_color', 'secondary_color']
        }),
        ('Features Section', {
            'fields': ['features_title', 'features_description',
                      'design_title', 'design_description']
        }),
        ('Images', {
            'fields': ['hero_image', 'features_image', 'design_image', 
                      'engine_image', 'transmission_image', 
                      'chassis_image', 'dimensions_image']
        }),
        ('Technical Specifications', {
            'fields': [
                # Engine
                ('engine_type', 'displacement'),
                ('bore_stroke', 'compression_ratio'),
                ('max_power', 'max_torque'),
                ('fuel_system', 'fuel_tank_capacity'),
                # Transmission
                ('clutch_type', 'transmission_type'),
                # Chassis
                ('frame_type', 'front_suspension'),
                ('rear_suspension', 'front_brake'),
                ('rear_brake', 'front_tyre'),
                ('rear_tyre',),
                # Dimensions
                ('dimensions', 'wheelbase'),
                ('ground_clearance', 'seat_height'),
                ('kerb_weight',)
            ],
            'classes': ['collapse']
        }),
    ]