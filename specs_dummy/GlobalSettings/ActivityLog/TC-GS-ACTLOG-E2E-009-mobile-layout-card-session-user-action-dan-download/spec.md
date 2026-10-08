---
id: TC-GS-ACTLOG-E2E-009-mobile-layout-card-session-user-action-dan-download
title: "Mobile Layout Card List Session, User Action, dan Download Seluruh Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-24
  - TC-GS-ACTLOG-25
  - TC-GS-ACTLOG-26
  - TC-GS-ACTLOG-140
coverage:
  web: automated
---

# Mobile Layout Card List Session, User Action, dan Download Seluruh Kolom

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Viewport diatur pada ukuran mobile (< 768px, misal 375x812)
- Terdapat entri Session dan User Action

## Test Steps

### Mobile Guided Tooltip
1. Buka halaman Activity Log pada viewport mobile.
2. Verifikasi Step 2 walkthrough menyorot tombol [⋯] di toolbar mobile (bukan icon filter desktop).
### Card List Tab Session
3. Buka Tab Session pada viewport mobile.
4. Verifikasi data ditampilkan sebagai Card List, bukan tabel lebar.
5. Verifikasi kartu log menampilkan: Baris 1 (Activity, Status, dan Timestamp); Baris 2 (User, Employee ID, Position, Division); Baris 3 (IP Address); Baris 4 (Note).
6. Verifikasi kolom Device / Browser tidak dimunculkan pada kartu mobile (sengaja dikecualikan untuk efisiensi ruang).
7. Untuk user tanpa Position, verifikasi sel nilai Position menampilkan tanda '—'.
### Card List Tab User Action
8. Buka Tab User Action pada viewport mobile.
9. Verifikasi kartu mutasi menampilkan: Baris 1 (Action, Object, Name, dan Timestamp); Baris 2 (Field: Old Value → New Value); Baris 3 ('by [Modified By]').
10. Untuk entri Create, verifikasi Old Value menampilkan '—'. Untuk Delete, New Value menampilkan '—'.
### Toolbar Mobile & Ekspor Penuh
11. Klik tombol [⋯] pada toolbar mobile, buka opsi Download.
12. Pilih Download as CSV pada Tab Session.
13. Verifikasi berkas CSV yang diunduh memuat seluruh 10 kolom lengkap (termasuk Device / Browser) karena antarmuka mobile tidak memiliki fitur Setup Column.
14. Buka Tab User Action dan unduh berkas XLSX via toolbar [⋯], verifikasi memuat seluruh 8 kolom lengkap.

## Notes

- Layout mobile mengoptimalkan pembacaan log pada layar sentuh tanpa menghilangkan kelengkapan data saat diekspor.
