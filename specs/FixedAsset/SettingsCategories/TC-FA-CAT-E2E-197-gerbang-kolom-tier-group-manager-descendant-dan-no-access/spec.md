---
id: TC-FA-CAT-E2E-197-gerbang-kolom-tier-group-manager-descendant-dan-no-access
title: "Gerbang Kolom Popup Detail Tier Group Manager: Asset Value, Warranty, dan Purchasing pada Group Ditugaskan beserta Descendant, No access di Luar, Accounting Tidak Tersedia"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-685
coverage:
  web: automated
---

# Gerbang Kolom Popup Detail Tier Group Manager: Asset Value, Warranty, dan Purchasing pada Group Ditugaskan beserta Descendant, No access di Luar, Accounting Tidak Tersedia

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager Capability CRUD (Pre-setup #9) `gmCapability_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_GMCAP_PASSWORD`; aktor ditugaskan pada group `Head Office` beserta descendant. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca (tidak diubah): Pre-setup #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), #22 (aset `Laptop Dell - 1` pada Group `Head Office > Floor 1 > Room 301`, `Laptop Dell - 3`, dan `Laptop HP - 3` pada Group `Region Jawa > Jakarta Selatan Distribution Center`), #55 (Asset Value dan Warranty Expiry: `Laptop Dell - 1` Warranty Expiry 2027-03-15; `Laptop Dell - 3` tanpa nilai), #56 (Custom Field Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO` dengan `Laptop Dell - 1` `PO-0001`; Accounting `Kode Anggaran`; lisensi FA-7 aktif).
- Kemampuan teknis: pemulihan konfigurasi kolom Setup Column dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`), dipakai sebagai langkah penghubung dan di hook `after` suite; disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-685: Tier Group Manager, gerbang per group ditugaskan beserta descendant

1. Pilih node `Electronics` pada sidebar
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`
4. Verifikasi daftar kolom Custom Field memuat kolom Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, dan `Nomor PO`
5. Verifikasi daftar kolom Custom Field tidak memuat kolom Accounting `Kode Anggaran`
6. Centang `Asset Value`, `Warranty Expiry`, dan `Nomor PO`, lalu klik `[Save]`
7. Verifikasi sel Asset Value `Laptop Dell - 1` menampilkan nilai (bukan `No access`)
8. Verifikasi sel Warranty Expiry `Laptop Dell - 1` menampilkan `2027-03-15`
9. Verifikasi sel `Nomor PO` `Laptop Dell - 1` menampilkan `PO-0001`
10. Verifikasi `Laptop Dell - 3` menampilkan `Pending` pada Asset Value (berhak, Purchase Cost belum ada) dan `—` pada Warranty Expiry dan `Nomor PO` (berhak, nilai belum ada)
11. Verifikasi sel Asset Value, Warranty Expiry, dan `Nomor PO` `Laptop HP - 3` menampilkan `No access`
12. Hover sel `No access` Asset Value `Laptop HP - 3`
13. Verifikasi tooltip `Requires View asset value access in this group.`
14. Hover sel `No access` Warranty Expiry `Laptop HP - 3`
15. Verifikasi tooltip `Requires Manage purchase access in this group.`
16. Hover sel `No access` `Nomor PO` `Laptop HP - 3`
17. Verifikasi tooltip `Requires Manage purchase access in this group.`
18. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 (memilih node sidebar) dan langkah 18 (menutup popup dan memulihkan konfigurasi kolom).
- Post Condition TC-FA-CAT-685 ("dikembalikan lewat `[Reset to Default]` lalu `[Save]`") dipenuhi dengan menghapus preferensi kolom di browser sesuai konvensi bagian 4; kemampuan disediakan tim FE.
- Absence pada langkah 5 diawali anchor positif pada surface yang sama (langkah 4: kolom Purchasing di daftar Setup Column tampil).
- Tier Total Control, Default User, dan Read Only ada di spec 198; tier Accounting Global dan Tanpa Hak Nilai Sensitif di spec 154.
- Temuan untuk QA:
  - TC-FA-CAT-685 Expected b menyebut "menampilkan Asset Value" pada `Laptop Dell - 1` tanpa angka, padahal Pre-setup #55 memberi 15000000.00 untuk aset itu; spec memverifikasi nilai tampil (bukan `No access`).
  - Tooltip pada langkah 13 sampai 17 diambil dari Expected e yang menyebut hover tiga kolom dalam satu kalimat; spec memverifikasi per kolom.
