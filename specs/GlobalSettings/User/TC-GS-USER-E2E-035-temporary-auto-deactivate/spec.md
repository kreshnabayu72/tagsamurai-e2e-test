---
id: TC-GS-USER-E2E-035-temporary-auto-deactivate
title: Temporary User nonaktif otomatis saat expiry tercapai
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-67
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
5. Buka Changelog dan System Log user "Cahyo Sementara"
6. Verifikasi ada entri nonaktif otomatis karena expiry dengan aktor "System"

## Notes

- PRD `user.md` [F-USER-09]: melewati Temporary Until membuat sistem menonaktifkan user tanpa dialog, dengan log Changelog aktor `System`.
- Aset atau approval yang menggantung setelah nonaktif otomatis ditangani Total Control (`USER-LOGIC-05`) dan tidak diuji di spec ini.
- Reaktivasi user yang sudah expired dicakup `TC-GS-USER-E2E-036-reaktivasi-temporary-expired`.
