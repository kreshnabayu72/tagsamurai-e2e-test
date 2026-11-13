---
id: TC-FA-FAREG-UI-001-tab-registration-sub-tab
title: "Tab Registration: sub tab, breadcrumb halaman utama, dan konfigurasi kolom antar tabel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r1", "§4.1#p1", "§4.1#p3", "§4.2.1#p1", "EB-KOL-3"]
smoke: []
dependsOn: []
trace:
  "§4.1#r1": 2
  "§4.1#p1": 3
  "§4.1#p3": [4, 5]
  "§4.2.1#p1": [7, 9, 11]
  EB-KOL-3: [16, 18, 20]
anchor: [15]
coverage:
  web: automated
---

# Tab Registration: sub tab, breadcrumb halaman utama, dan konfigurasi kolom antar tabel

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration.
- Komponen: Tab `Registration`
- Data:
  - DU-001-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `09/11/26, 08:15`.
  - DU-001-2: pengajuan Waiting for Approval Registration ID `REG-20261109-00003`, Group `Gudang 1`, Total Asset `12`, Requested By `Rina W`, Last Updated `09/11/26, 10:20`.
  - DU-001-3: pengajuan History Registration ID `REG-20261104-00009`, Group `Gudang 1`, Total Asset `12`, Status `Approved`, Requested By `Rina W`, Approver `Budi S`, Last Updated `04/11/26, 15:30`.
- Kondisi:
  - K1: sub tab Draft berisi DU-001-1, sub tab Waiting for Approval berisi DU-001-2, sub tab History berisi DU-001-3.

## Test Steps

### Susunan sub tab dan sub tab awal
1. Tampilkan Tab `Registration` dengan kondisi K1
2. Verifikasi sub tab `Draft`, `Waiting for Approval`, dan `History` tampil berurutan
3. Verifikasi sub tab `Draft` aktif
4. Verifikasi judul pill `Waiting for Approval` tidak memuat jumlah
5. Verifikasi judul pill `History` tidak memuat jumlah

### Breadcrumb halaman utama mengikuti sub tab aktif
6. Tampilkan Tab `Registration` dengan kondisi K1
7. Verifikasi breadcrumb `Assets > Registration > Draft`
8. Klik sub tab `Waiting for Approval`
9. Verifikasi breadcrumb `Assets > Registration > Waiting for Approval`
10. Klik sub tab `History`
11. Verifikasi breadcrumb `Assets > Registration > History`

### Konfigurasi kolom satu tabel tidak mengubah tabel lain
12. Tampilkan Tab `Registration` dengan kondisi K1
13. Klik header kolom Actions `⋯` pada tabel sub tab `Draft`
14. Hilangkan centang kolom `Total Asset` pada panel Column Visibility
15. Verifikasi kolom `Group` tampil pada tabel sub tab `Draft`
16. Verifikasi kolom `Total Asset` tidak tampil pada tabel sub tab `Draft`
17. Klik sub tab `Waiting for Approval`
18. Verifikasi kolom `Total Asset` tampil pada tabel sub tab `Waiting for Approval`
19. Klik sub tab `History`
20. Verifikasi kolom `Total Asset` tampil pada tabel sub tab `History`
