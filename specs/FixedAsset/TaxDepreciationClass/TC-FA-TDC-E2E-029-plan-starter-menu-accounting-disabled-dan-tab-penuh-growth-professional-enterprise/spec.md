---
id: TC-FA-TDC-E2E-029-plan-starter-menu-accounting-disabled-dan-tab-penuh-growth-professional-enterprise
title: "Plan Starter: Menu Accounting Disabled dan Akses Langsung Ditolak, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-98
  - TC-FA-TDC-100
  - TC-FA-TDC-764
  - TC-FA-TDC-765
sourceRules: ["§9.10#b2", "E-FATDC-67", "§9.10#b1", "§4.1.5#r1", "§4.1.5#r2", "§4.1.5#r3", "§4.1.5#r4", "§4.1.5#r5", "§4.1.5#r6", "§4.1.5#r7", "§4.8#r9"]
smoke: []
dependsOn: []
trace:
  "§9.10#b2": [3, 6, 14, 16]
  "E-FATDC-67": [6, 9, 16]
  "§9.10#b1": 20
  "§4.1.5#r1": 21
  "§4.1.5#r2": 21
  "§4.1.5#r3": 21
  "§4.1.5#r4": 21
  "§4.1.5#r5": 21
  "§4.1.5#r6": 21
  "§4.1.5#r7": 21
  "§4.8#r9": 22
anchor: [5, 8, 10]
coverage:
  web: automated
---

# Plan Starter: Menu Accounting Disabled dan Akses Langsung Ditolak, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control dan Read Only. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (Total Control) dan `Spectra.env.FA_RO_PASSWORD` (Read Only); kedua nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` dan didaftarkan tim FE.
- Tabel "Company uji" (disediakan tim FE; plan company tidak diubah oleh spec ini):

| Company | Plan | Akun yang dipakai |
|---|---|---|
| Company Starter | Starter | Total Control, Read Only |
| Company Growth | Growth | Total Control |
| Company Professional | Professional | Total Control |
| Company Enterprise | Enterprise | Total Control |

- Data Pre-setup: pada company Growth, Professional, dan Enterprise tabel berisi 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) yang belum diubah; spec hanya membaca data ini. URL tab Tax Depreciation Class: `Fixture.fixedAssetTaxDepreciationClass.tabUrl` (fixture belum ada, disediakan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada Company Starter; hook `after` mengembalikan sesi ke akun default suite. Spec ini membuka layarnya sendiri (plan Starter tidak dapat membuka halaman Accounting), sehingga halaman tidak dibuka hook `beforeEach` suite.
- Spec ini tidak mengubah plan atau data apa pun; tidak ada state global yang perlu dipulihkan selain sesi login.
- Rujukan suite: `suite.md` (hook `before` dan `after`, `beforeEach`).

## Test Steps

### Plan Starter, Total Control (TC-FA-TDC-98 butir a, TC-FA-TDC-764, TC-FA-TDC-765)

1. Buka sidebar Fixed Asset (FAMS)
2. Arahkan kursor ke menu `Accounting`
3. Verifikasi menu `Accounting` tampil Disabled dengan chip `Upgrade`
4. Klik menu `Accounting`
5. Verifikasi sedikitnya satu item menu sidebar lain tampil
6. Verifikasi halaman Settings > Accounting dan tab Tax Depreciation Class tidak terbuka
7. Ketik `Fixture.fixedAssetTaxDepreciationClass.tabUrl` langsung di address bar
8. Verifikasi toast error `You don't have permission to do this.` tampil
9. Verifikasi isi tab Tax Depreciation Class (tabel, toolbar, dan tombol `+ Class`) tidak tampil untuk Total Control
10. Verifikasi tidak ada redirect ke halaman unauthorized terpisah

### Plan Starter, Read Only (TC-FA-TDC-98 butir b)

11. Logout
12. Login sebagai Read Only pada Company Starter
13. Buka sidebar Fixed Asset (FAMS)
14. Verifikasi menu `Accounting` tampil Disabled dengan chip `Upgrade`
15. Klik menu `Accounting`
16. Verifikasi halaman Settings > Accounting tidak terbuka

### Plan Growth, Professional, dan Enterprise (TC-FA-TDC-100)

Untuk setiap company pada tabel "Company uji" dengan plan Growth, Professional, dan Enterprise (langkah 17 sampai 22):

17. Logout
18. Login sebagai Total Control pada company tersebut
19. Buka Settings > Accounting > Tax Depreciation Class
20. Verifikasi tab terbuka
21. Verifikasi 7 baris seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) tampil
22. Verifikasi tombol `+ Class` Show di toolbar

## Notes

- Langkah penghubung: langkah 11 dan 12 (Logout lalu login Read Only) dan langkah 17 dan 18 (ganti akun dan company) adalah ganti akun eksplisit (S-07); langkah 5 adalah anchor positif untuk absence halaman (8b.2); langkah 13 membuka sidebar tanpa asersi.
- Pembagian TC lintas langkah: TC-FA-TDC-98 butir a (Total Control) dan TC-FA-TDC-764 mengamati keadaan yang sama (menu `Accounting` Disabled dengan chip `Upgrade`, halaman tidak terbuka); satu rangkaian langkah 1 sampai 6 memenuhi keduanya, `Verifikasi` langkah 3 dan 6 memetakan butir a TC-98 dan butir a dan b TC-764. TC-FA-TDC-98 butir b ada di langkah 14 dan 16.
- Langkah 17 sampai 22 diulang tiga kali (Growth, Professional, Enterprise); parameter tiap iterasi ada di tabel "Company uji" (8b.7). Ekspansi: 34 langkah.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan nama company untuk Total Control dan Read Only pada tiap plan; disediakan tim FE.
  - TC-FA-TDC-765 tidak memberi URL tab; spec memakai fixture `tabUrl` (disediakan tim FE).
  - TC-FA-TDC-98 dan TC-FA-TDC-764 tumpang tindih untuk Total Control pada plan Starter (Expected sama); ditulis sebagai satu rangkaian langkah.
  - TC-FA-TDC-100 menyebut 7 class seed pada tiap company tanpa Class Code kolom Active; spec hanya menyalin daftar kode seed.
