---
id: TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab
title: "Screening 3 Zona Tab Session dan User Action, Navigasi Tab, serta Tab Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-01
  - TC-GS-ACTLOG-02
  - TC-GS-ACTLOG-03
  - TC-GS-ACTLOG-227
coverage:
  web: automated
---

# Screening 3 Zona Tab Session dan User Action, Navigasi Tab, serta Tab Default

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di modul Global Settings
- Terdapat data log aktivitas Session dan User Action di entitas aktif

## Test Steps

### Screening Awal & Tab Default
1. Buka menu Global Settings > Activity Log di navigasi sidebar.
2. Verifikasi Tab Session aktif secara default saat pertama kali masuk ke halaman Activity Log.
3. Verifikasi Breadcrumb di header menampilkan 'Activity Log > Session' dan segmen terakhir bukan link.
4. Verifikasi Tab bar menampilkan dua tab: 'Session (aktif)' dan 'User Action'.
5. Verifikasi toolbar Table Tools di sisi kanan memuat: Search, Filter, dan Download tanpa tombol create (modul read-only).
6. Verifikasi tabel Tab Session menampilkan 10 kolom: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device / Browser, serta header kolom Column Visibility (⋯).
7. Verifikasi body tabel per baris tidak memiliki tombol aksi (tanpa row action).
8. Verifikasi footer tabel menampilkan paginasi default 10 baris per halaman.
### Navigasi Tab & Breadcrumb
9. Klik tab 'User Action'.
10. Verifikasi Tab User Action kini dalam status aktif dan Tab Session tidak aktif.
11. Verifikasi Breadcrumb diperbarui menjadi 'Activity Log > User Action'.
12. Verifikasi tabel Tab User Action menampilkan 8 kolom: Date, Action, Object, Name, Field, Old Value, New Value, Modified By, serta header Column Visibility (⋯).
13. Lakukan refresh halaman (F5) saat berada di Tab User Action.
14. Verifikasi setelah refresh halaman tetap berada pada Tab User Action.
15. Klik kembali tab 'Session' dan refresh halaman (F5), verifikasi halaman tetap berada pada Tab Session.

## Notes

- Modul Activity Log adalah modul audit read-only murni tanpa operasi create, edit, atau delete record langsung.
