from typing import Any

# ---------------------------------------------------------------------------
# Depots
# ---------------------------------------------------------------------------

MOCK_DEPOTS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Main Campus Depot",
        "location": "Gate 1, Central Campus, Block A",
        "capacity": 40,
    },
    {
        "id": 2,
        "name": "North Wing Garage",
        "location": "North Wing, Academic Zone, Block N",
        "capacity": 25,
    },
    {
        "id": 3,
        "name": "Research Park Annex",
        "location": "Research & Innovation Park, South Campus",
        "capacity": 15,
    },
]

# ---------------------------------------------------------------------------
# Vehicles
# ---------------------------------------------------------------------------

MOCK_VEHICLES: list[dict[str, Any]] = [
    {
        "id": 101,
        "depot_id": 1,
        "type": "Electric Shuttle",
        "status": "Active",
        "last_maintenance_date": "2025-04-10",
    },
    {
        "id": 102,
        "depot_id": 1,
        "type": "Diesel Bus",
        "status": "Maintenance",
        "last_maintenance_date": "2025-03-22",
    },
    {
        "id": 103,
        "depot_id": 1,
        "type": "Electric Shuttle",
        "status": "Active",
        "last_maintenance_date": "2025-05-01",
    },
    {
        "id": 104,
        "depot_id": 1,
        "type": "Cargo Van",
        "status": "In Transit",
        "last_maintenance_date": "2025-04-28",
    },
    {
        "id": 105,
        "depot_id": 2,
        "type": "Minibus",
        "status": "Active",
        "last_maintenance_date": "2025-04-15",
    },
    {
        "id": 106,
        "depot_id": 2,
        "type": "Electric Shuttle",
        "status": "Active",
        "last_maintenance_date": "2025-05-05",
    },
    {
        "id": 107,
        "depot_id": 2,
        "type": "Ambulance",
        "status": "Active",
        "last_maintenance_date": "2025-05-10",
    },
    {
        "id": 108,
        "depot_id": 2,
        "type": "Diesel Bus",
        "status": "Maintenance",
        "last_maintenance_date": "2025-02-18",
    },
    {
        "id": 109,
        "depot_id": 3,
        "type": "Electric Car",
        "status": "Active",
        "last_maintenance_date": "2025-04-30",
    },
    {
        "id": 110,
        "depot_id": 3,
        "type": "Cargo Van",
        "status": "In Transit",
        "last_maintenance_date": "2025-03-09",
    },
]

# ---------------------------------------------------------------------------
# Notifications
# ---------------------------------------------------------------------------

MOCK_NOTIFICATIONS: list[dict[str, Any]] = [
    {
        "id": 1,
        "type": "Alert",
        "message": "Vehicle #102 is overdue for its 6-month service inspection.",
        "is_read": False,
        "timestamp": 1747305600,
    },
    {
        "id": 2,
        "type": "Info",
        "message": "Shuttle route C3 will resume normal operations from Monday.",
        "is_read": True,
        "timestamp": 1747392000,
    },
    {
        "id": 3,
        "type": "Warning",
        "message": "North Wing Garage capacity at 88%. Consider redistributing vehicles.",
        "is_read": False,
        "timestamp": 1747478400,
    },
    {
        "id": 4,
        "type": "Info",
        "message": "Scheduled maintenance window: Depot 1 systems offline 02:00–04:00 IST on 20 May.",
        "is_read": True,
        "timestamp": 1747564800,
    },
    {
        "id": 5,
        "type": "Alert",
        "message": "Vehicle #108 brake fluid levels critically low. Immediate inspection required.",
        "is_read": False,
        "timestamp": 1747651200,
    },
    {
        "id": 6,
        "type": "Warning",
        "message": "Fuel consumption for Diesel Bus fleet is 18% above monthly baseline.",
        "is_read": False,
        "timestamp": 1747737600,
    },
    {
        "id": 7,
        "type": "Info",
        "message": "Electric Shuttle #103 successfully completed 10,000 km milestone.",
        "is_read": True,
        "timestamp": 1747824000,
    },
    {
        "id": 8,
        "type": "Alert",
        "message": "Campus emergency drill scheduled for 16 May. All non-essential vehicles must be cleared from Gate 1.",
        "is_read": False,
        "timestamp": 1747910400,
    },
    {
        "id": 9,
        "type": "Info",
        "message": "New parking bay allocation policy effective from 1 June. Refer to updated SOP.",
        "is_read": True,
        "timestamp": 1747996800,
    },
    {
        "id": 10,
        "type": "Warning",
        "message": "Vehicle #110 GPS tracker offline since 14 May 09:30 IST.",
        "is_read": False,
        "timestamp": 1748083200,
    },
    {
        "id": 11,
        "type": "Alert",
        "message": "Tyre pressure anomaly detected on Vehicle #104. Inspection dispatched.",
        "is_read": False,
        "timestamp": 1748169600,
    },
    {
        "id": 12,
        "type": "Info",
        "message": "Research Park Annex depot capacity upgraded to 20 units from Q3 2025.",
        "is_read": True,
        "timestamp": 1748256000,
    },
    {
        "id": 13,
        "type": "Warning",
        "message": "Electric charging station 4 at North Wing is reporting intermittent faults.",
        "is_read": False,
        "timestamp": 1748342400,
    },
    {
        "id": 14,
        "type": "Info",
        "message": "Ambulance #107 quarterly compliance check completed. Certificate valid until Nov 2025.",
        "is_read": True,
        "timestamp": 1748428800,
    },
    {
        "id": 15,
        "type": "Alert",
        "message": "Unauthorized vehicle access detected at Research Park Annex gate at 23:47.",
        "is_read": False,
        "timestamp": 1748515200,
    },
    {
        "id": 16,
        "type": "Warning",
        "message": "Cargo Van #104 coolant temperature exceeded threshold on last trip log.",
        "is_read": False,
        "timestamp": 1748601600,
    },
    {
        "id": 17,
        "type": "Info",
        "message": "Fleet management system downtime scheduled for 22 May 01:00–03:00 IST.",
        "is_read": True,
        "timestamp": 1748688000,
    },
    {
        "id": 18,
        "type": "Alert",
        "message": "Vehicle #105 missed its scheduled service slot on 13 May. Rescheduling required.",
        "is_read": False,
        "timestamp": 1748774400,
    },
    {
        "id": 19,
        "type": "Info",
        "message": "Driver orientation programme for new Electric Shuttle operators on 25 May.",
        "is_read": True,
        "timestamp": 1748860800,
    },
    {
        "id": 20,
        "type": "Warning",
        "message": "Main Campus Depot CCTV system requires firmware update by 31 May.",
        "is_read": False,
        "timestamp": 1748947200,
    },
    {
        "id": 21,
        "type": "Alert",
        "message": "Vehicle #101 airbag sensor diagnostic fault logged. Suspend active service pending review.",
        "is_read": False,
        "timestamp": 1749033600,
    },
    {
        "id": 22,
        "type": "Info",
        "message": "Monthly vehicle utilisation report for April 2025 is now available in the portal.",
        "is_read": True,
        "timestamp": 1749120000,
    },
    {
        "id": 23,
        "type": "Warning",
        "message": "Battery degradation detected on Electric Shuttle #106. Schedule cell health check.",
        "is_read": False,
        "timestamp": 1749206400,
    },
    {
        "id": 24,
        "type": "Info",
        "message": "Holiday schedule for fleet operations during summer recess published.",
        "is_read": True,
        "timestamp": 1749292800,
    },
    {
        "id": 25,
        "type": "Alert",
        "message": "Depot 2 fire suppression system annual test due on 30 May. Co-ordinate with Facilities.",
        "is_read": False,
        "timestamp": 1749379200,
    },
]
