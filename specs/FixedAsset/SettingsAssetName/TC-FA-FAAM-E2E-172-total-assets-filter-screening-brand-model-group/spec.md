---
id: TC-FA-FAAM-E2E-172-total-assets-filter-screening-brand-model-group
title: "Tab Total Assets Filter: Screening Panel, Opsi Brand-Model DISTINCT, dan Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-511
  - TC-FA-FAAM-512
  - TC-FA-FAAM-513
coverage:
  web: automated
---

# Tab Total Assets Filter: Screening Panel, Opsi Brand-Model DISTINCT, dan Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset contoh Pre-setup #26; Brand `Dell`; model `3310` dan `5420` dipakai aset yang tampil, model `7420` hanya dirujuk aset Deleted dan Disposed, Pre-setup #10i; Group `Head Office`, `Finance`, `Warehouse`).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-511: Screening Filter Panel Tab Total Assets

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Klik icon Filter
3. Verifikasi field `TAG` dengan placeholder `All tags`
4. Verifikasi field `Brand` dengan placeholder `All brands`
5. Verifikasi field `Model/Type` dengan placeholder `All models`
6. Verifikasi field `Measurement` dengan placeholder `All units`
7. Verifikasi field `Category` dengan placeholder `All categories` (tombol Modal Tree Picker)
8. Verifikasi field `Group` dengan placeholder `All groups`
9. Verifikasi field `Label` dengan placeholder `All labels`
10. Verifikasi field `Status` dengan placeholder `All statuses`
11. Verifikasi field `Transactional Policy` dengan placeholder `All transactions`
12. Verifikasi field `Last Scanned` dengan placeholder `Select date`
13. Verifikasi field `Asset Value` dengan placeholder `Min` dan `Max`
14. Verifikasi field `Warranty Expiry` dengan placeholder `Select date`
15. Verifikasi field `Last Updated` dengan placeholder `Select date`
16. Verifikasi `[Clear Field]` dan `[Apply]` tampil
17. Verifikasi tidak ada filter untuk Name
18. Verifikasi tidak ada filter untuk kolom custom field bertipe Text, Text Area, Phone, Email, URL, Document, dan Formula (kolom custom field bertipe lain memiliki field Filter menurut Data Type; TC-FA-FAAM-810 sampai 813)

### TC-FA-FAAM-512: Opsi filter Brand dan Model/Type hanya nilai yang muncul pada data tabel

19. Buka dropdown Brand pada Filter Panel
20. Verifikasi opsi Brand hanya `Dell`
21. Buka dropdown Model/Type pada Filter Panel
22. Verifikasi opsi Model/Type `3310` dan `5420`
23. Verifikasi `7420` tidak muncul walau merupakan model Asset Name

### TC-FA-FAAM-513: Filter Group multi-select dengan opsi DISTINCT dari tabel

24. Buka dropdown Group pada Filter Panel
25. Verifikasi opsi Group berasal dari data tabel (`Head Office`, `Finance`, `Warehouse`)
26. Pilih Group `Finance` dan `Warehouse`, klik `[Apply]`
27. Verifikasi sedikitnya satu baris tampil pada hasil
28. Verifikasi hasil OR dalam field: seluruh baris berGroup `Finance` atau `Warehouse`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Filter Panel tetap terbuka dari TC-FA-FAAM-511 ke TC-FA-FAAM-512 (TC memakai satu pembukaan Filter Panel untuk screening dan pengecekan opsi); pada TC-FA-FAAM-513 Filter Panel dipakai sebelum `[Apply]`.
- Langkah penghubung: tidak ada selain pembukaan dropdown untuk pembacaan opsi.
- Temuan untuk QA:
  - TC-FA-FAAM-512 mengasersi opsi `7420` tidak muncul memakai model yang hanya dirujuk aset Deleted dan Disposed (Pre-setup #10i); TC-FA-FAAM-513 tidak menyebut daftar opsi Group yang diharapkan secara eksplisit (nilai di atas diturunkan dari Pre-setup #26).
