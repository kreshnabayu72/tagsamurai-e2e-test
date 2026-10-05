---
id: TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual
title: "Tab Session: Struktur 6 field Filter Panel dan penerapan filter individual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-42
  - TC-GS-ACTLOG-43
  - TC-GS-ACTLOG-44
  - TC-GS-ACTLOG-45
  - TC-GS-ACTLOG-46
  - TC-GS-ACTLOG-47
  - TC-GS-ACTLOG-48
  - TC-GS-ACTLOG-49
  - TC-GS-ACTLOG-241
coverage:
  web: automated
---

# Tab Session: Struktur 6 field Filter Panel dan penerapan filter individual

## Prerequisites

- Login sebagai Role: Total Control
- Tab Session memuat variasi entri Login, Logout, Session, Change Password, dan Reset Password

## Test Steps

1. Buka Tab Session lalu klik icon Filter
2. Verifikasi struktur 6 field Filter Panel berurutan: Date, User, Position, Division, Activity, dan Status
3. Pilih satu tanggal spesifik pada field Date lalu klik `[Apply]`
4. Verifikasi hanya entri pada tanggal tersebut yang tampil di tabel
5. Buka kembali Filter, kosongkan Date, pilih 2 user pada field User lalu klik `[Apply]`
6. Verifikasi hanya entri milik kedua user tersebut yang tampil
7. Ulangi penyaringan untuk field Position dan Division, verifikasi data tersaring sesuai opsi terpilih
8. Buka Filter, pilih Activity "Login" dan "Logout" lalu klik `[Apply]`
9. Verifikasi hanya aktivitas Login dan Logout yang tampil
10. Buka Filter, pilih Activity "Session" saja lalu klik `[Apply]`
11. Verifikasi hanya aktivitas Session yang tampil
12. Buka Filter, pilih Activity "Change Password" saja lalu klik `[Apply]`
13. Verifikasi entri Change Password tampil dengan kolom Status Success atau Failed (bukan strip)
14. Buka Filter, pilih Status "Failed" saja lalu klik `[Apply]`
15. Verifikasi hanya entri berstatus Failed yang tampil dan entri Logout/Session (berstatus strip) tidak ikut muncul

## Notes

- Entri Logout dan Session memiliki representasi status visual `—` di tabel sehingga dikecualikan dari filter Status Failed.
