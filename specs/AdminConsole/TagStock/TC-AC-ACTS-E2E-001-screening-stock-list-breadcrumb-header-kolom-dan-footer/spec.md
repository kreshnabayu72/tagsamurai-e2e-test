---
id: TC-AC-ACTS-E2E-001-screening-stock-list-breadcrumb-header-kolom-dan-footer
title: "Screening Stock List: Breadcrumb, Header, Kolom, Footer, Urutan Default, Tanpa Checkbox, dan Aria-Label Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-1
  - TC-AC-ACTS-15
  - TC-AC-ACTS-33
  - TC-AC-ACTS-34
  - TC-AC-ACTS-35
  - TC-AC-ACTS-812
coverage:
  web: automated
---

# Screening Stock List: Breadcrumb, Header, Kolom, Footer, Urutan Default, Tanpa Checkbox, dan Aria-Label Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS (#12 sampai #16). Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Tidak ada data Dinamis sehingga tidak ada suffix `{runId}` dan tidak ada seeding.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-34: Screening Stock List: header, kolom, footer

1. Amati seluruh tampilan Stock List dari atas ke bawah
2. Verifikasi Breadcrumb `TAG > Stock` tampil
3. Verifikasi Table Tools berisi `Search | Filter | Download`
4. Verifikasi Kolom berurutan `Photo (unsortable) | Device Name (sortable) | SKU (sortable) | TAG Type (sortable) | Type (sortable) | Brand (sortable) | Model/Type (sortable) | Total Registered (sortable) | Available (sortable) | In Use (sortable) | Damaged/Missing (sortable) | Last Updated (sortable) | Column Visibility (⋯)`
5. Verifikasi Header `Column Visibility (⋯)` unsortable: klik header membuka Overlay Column Visibility, dan body per baris berupa row action menu
6. Verifikasi Footer pagination default 10 data per halaman

### TC-AC-ACTS-35: Default sort Last Updated Newest First

7. Amati urutan baris dan indikator sort pada header kolom
8. Verifikasi Baris terurut Last Updated Newest First (SKU tanpa aktivitas di akhir) saat halaman dibuka
9. Verifikasi Tidak ada panah sort aktif pada kolom lain

### TC-AC-ACTS-1: Breadcrumb Stock List tanpa Page Title

10. Amati area atas halaman
11. Verifikasi Breadcrumb tampil `TAG > Stock`
12. Verifikasi Tidak ada Page Title terpisah di bawah breadcrumb
13. Klik segmen `TAG` pada breadcrumb
14. Klik segmen `Stock` pada breadcrumb
15. Verifikasi Kedua segmen adalah label statis (breadcrumb 2 segmen), klik tidak membuka halaman lain

### TC-AC-ACTS-15: Stock List tanpa checkbox, Select All, atau bulk action

16. Verifikasi Stock List memuat sedikitnya satu baris SKU
17. Amati kolom paling kiri dan area toolbar
18. Hover salah satu baris
19. Verifikasi Tidak ada kolom checkbox, tombol Select All, maupun Bulk Action Bar

### TC-AC-ACTS-33: Toolbar tanpa icon Activity Log

20. Amati toolbar
21. Verifikasi Toolbar hanya memuat Search, Filter, dan Download
22. Verifikasi Tidak ada icon Activity Log dan tidak ada Activity Log

### TC-AC-ACTS-812: Aria-label tabel

23. Periksa atribut aria-label tabel Stock List
24. Verifikasi Tabel Stock List memiliki aria-label `TAG Stock` (tanpa `[SKU]` maupun TAG Type)

## Notes

- Urutan TC: TC-AC-ACTS-34 dan TC-AC-ACTS-35 (keadaan awal halaman) dijalankan lebih dulu agar tidak terpengaruh klik pada TC lain; TC-AC-ACTS-1, 15, 33, dan 812 menyusul (S-10).
- Langkah penghubung (S-03): tidak ada. Halaman dibuka hook `beforeEach` suite sehingga langkah "Buka TAG > Stock" pada TC sumber tidak diulang.
- Temuan untuk QA (S-15): TC-AC-ACTS-1 butir c ("klik tidak membuka halaman lain") tidak menyebut cara asersi; spec mengasersinya lewat tidak adanya perpindahan halaman setelah klik. TC-AC-ACTS-34 menulis `(unsortable — header klik = buka Overlay Column Visibility ...)` dalam satu butir Expected; spec memisahkannya menjadi dua Verifikasi (daftar kolom dan perilaku header ⋯).
