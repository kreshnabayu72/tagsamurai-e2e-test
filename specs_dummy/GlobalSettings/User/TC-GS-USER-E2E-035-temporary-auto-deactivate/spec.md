---
id: TC-GS-USER-E2E-035-temporary-auto-deactivate
title: Temporary User nonaktif otomatis saat expiry tercapai
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-67
  - TC-GS-USER-114
coverage:
  web: automated
---

# Temporary User nonaktif otomatis saat expiry tercapai

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Cahyo Sementara" berstatus Active, Temporary, dengan Temporary Until hari ini
- Pemicu waktu yang disediakan tim FE: job nonaktif otomatis bisa dijalankan atau jam sistem bisa dimajukan melewati waktu expiry, sehingga sistem memproses expiry dalam waktu run
- Spec ini membuat "Cahyo Sementara" menjadi Inactive, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Buka User List dan verifikasi "Cahyo Sementara" berstatus Active dengan Temporary Until hari ini
2. Picu job nonaktif otomatis atau majukan waktu melewati expiry sesuai kebutuhan di Prerequisites
3. Muat ulang User List
4. Verifikasi Toggle Active pada baris "Cahyo Sementara" otomatis OFF (Inactive)
5. Buka Changelog user "Cahyo Sementara"
6. Verifikasi ada baris Action "Auto-Deactivate", Field "Status (Global)", Old Value "Active", New Value "Inactive", dan Modified By "System"
7. Buka Global Settings > Activity Log dan verifikasi baris yang sama muncul dengan Modified By "System"
8. Buka System Log akun admin yang login dan verifikasi tidak ada baris untuk nonaktif otomatis ini

## Notes

- PRD `user.md` [F-USER-09]: melewati Temporary Until membuat sistem menonaktifkan user tanpa dialog. Baris Auto-Deactivate ada di Changelog dan Activity Log dengan Modified By "System", dan tidak ada di System Log karena System Log butuh aktor manusia (bagian 8.3 dan 8.6).
- Aset atau approval yang menggantung setelah nonaktif otomatis ditangani Total Control (`USER-LOGIC-05`) dan tidak diuji di spec ini.
- Reaktivasi user yang sudah expired dicakup `TC-GS-USER-E2E-036-reaktivasi-temporary-expired`.
- `TC-GS-USER-114` (Changelog Auto-Deactivate dengan Modified By System) dicakup langkah Changelog di atas. Field di PRD `user.md` bagian 8.3 adalah `Status (Global)`.
