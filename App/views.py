from django.shortcuts import render

def products(request):
    products = [
        {"name": "Laptop", "price": 2500},
        {"name": "Mouse", "price": 80},
        {"name": "Keyboard", "price": 150},
        {"name": "Monitor", "price": 700},
        {"name": "Headphones", "price": 200},
        {"name": "Webcam", "price": 120},
        {"name": "Microphone", "price": 180},
        {"name": "Speakers", "price": 250},
        {"name": "Printer", "price": 400},
        {"name": "Scanner", "price": 350},
        {"name": "Tablet", "price": 1200},
        {"name": "Smartphone", "price": 1800},
        {"name": "Smartwatch", "price": 600},
        {"name": "USB Flash Drive", "price": 40},
        {"name": "External Hard Drive", "price": 300},
        {"name": "SSD", "price": 450},
        {"name": "RAM", "price": 220},
        {"name": "Graphics Card", "price": 1500},
        {"name": "Processor", "price": 900},
        {"name": "Motherboard", "price": 650},
        {"name": "Power Supply", "price": 280},
        {"name": "Computer Case", "price": 320},
        {"name": "CPU Cooler", "price": 180},
        {"name": "Wi-Fi Router", "price": 250},
        {"name": "Ethernet Cable", "price": 25},
        {"name": "HDMI Cable", "price": 35},
        {"name": "USB Hub", "price": 90},
        {"name": "Docking Station", "price": 350},
        {"name": "Laptop Stand", "price": 100},
        {"name": "Mouse Pad", "price": 30},
        {"name": "Mechanical Keyboard", "price": 300},
        {"name": "Gaming Mouse", "price": 180},
        {"name": "Gaming Headset", "price": 280},
        {"name": "Gaming Chair", "price": 850},
        {"name": "Desk Lamp", "price": 120},
        {"name": "Office Desk", "price": 900},
        {"name": "Office Chair", "price": 750},
        {"name": "Projector", "price": 1100},
        {"name": "TV", "price": 2200},
        {"name": "Soundbar", "price": 500},
        {"name": "Digital Camera", "price": 1600},
        {"name": "Camera Lens", "price": 800},
        {"name": "Tripod", "price": 150},
        {"name": "Ring Light", "price": 130},
        {"name": "Power Bank", "price": 140},
        {"name": "Phone Charger", "price": 50},
        {"name": "Wireless Charger", "price": 110},
        {"name": "Phone Case", "price": 45},
        {"name": "Screen Protector", "price": 20},
        {"name": "Bluetooth Speaker", "price": 170},
        {"name": "E-Reader", "price": 550},
        {"name": "Smart Home Hub", "price": 400},
        {"name": "Smart Bulb", "price": 60},
        {"name": "Security Camera", "price": 320},
        {"name": "Video Doorbell", "price": 450},
        {"name": "External DVD Drive", "price": 130},
        {"name": "Card Reader", "price": 35},
        {"name": "UPS Battery Backup", "price": 500},
        {"name": "Surge Protector", "price": 100},
        {"name": "NAS Storage", "price": 1400},
        {"name": "Graphics Tablet", "price": 650},
        {"name": "VR Headset", "price": 1900},
        {"name": "Game Controller", "price": 220},
        {"name": "Portable Monitor", "price": 600}
    ]

    context = {"products": products}


    return render(request,'products.html', context)


def home(request):

    return render(request,'home.html')