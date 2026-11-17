---
id: TC-FA-FAAC-E2E-019-navigasi-sidebar-tab-asset-class-dan-breadcrumb-dari-detail
title: "Navigasi Menu Accounting di Sidebar, Klik Tab Asset Class, dan Breadcrumb dari Detail"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-3
  - TC-FA-FAAC-4
  - TC-FA-FAAC-587
sourceRules: ["FAAC-LOGIC-18c", "§4.2a#p1", "FAAC-LOGIC-18a", "§3.10#p2"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-18c": 3
  "§4.2a#p1": [6, 7]
  "FAAC-LOGIC-18a": 9
  "§3.10#p2": 14
anchor: [4]
coverage:
  web: automated
---

# Navigasi Menu Accounting di Sidebar, Klik Tab Asset Class, dan Breadcrumb dari Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC (HEAVY-EQ dan delapan lainnya). Plan client dengan fitur Accounting & Depreciation tersedia. Seed disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-3: Buka halaman Accounting lewat sidebar setelah memakai tab Asset Class

1. Klik menu Dashboard di sidebar
2. Klik kembali menu Accounting di sidebar
3. Verifikasi tab `Preferences` (tab pertama) aktif, bukan tab `Asset Class`
4. Verifikasi panel langkah setup tidak ada pada halaman

### TC-FA-FAAC-4: Klik tab Asset Class dari tab Preferences

5. Klik tab Asset Class
6. Verifikasi tab `Asset Class` aktif dan tabel Asset Class tampil
7. Verifikasi breadcrumb berbunyi `Settings > Accounting > Asset Class`

### TC-FA-FAAC-587: Tab Asset Class tetap tab keempat dan dapat dicapai dari Detail

8. Klik menu Accounting di sidebar
9. Verifikasi tab berurutan `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, `Asset Class`
10. Klik tab Asset Class
11. Ketik Search `HEAVY-EQ`, tekan Enter
12. Klik link Class Code `HEAVY-EQ`
13. Klik breadcrumb `Asset Class`
14. Verifikasi tab `Asset Class` aktif

## Notes

- Langkah penghubung (S-03): langkah 10 (membuka tab Asset Class sebelum mengklik link Class Code, karena TC-FA-FAAC-587 langkah 2 mengandaikan tabel tampil) dan langkah 11 (Search untuk menemukan baris target; R-16). TC-FA-FAAC-3 langkah 1 dan 2 (klik menu Accounting lalu tab Asset Class) dipenuhi layar awal hook `beforeEach`; langkah 1 spec ini adalah langkah 3 TC.
- Temuan untuk QA:
  - TC-FA-FAAC-587 langkah 2 menyebut "salah satu Asset Class" tanpa menentukan baris; spec memakai HEAVY-EQ.
  - Post Condition TC-FA-FAAC-587 ("PRD tab saudara menunjuk ke FAAC-LOGIC-18") tidak punya langkah observasi dan tidak diasersi.
