---
id: TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog
title: "Dialog Unsaved Changes pada Popup Edit Unit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-86
  - TC-GS-UOM-87
  - TC-GS-UOM-273
coverage:
  web: automated
---

# Dialog Unsaved Changes pada Popup Edit Unit

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji perilaku menutup popup Edit Unit yang dirty.
- Kebutuhan mock (endpoint dari `global-settings/measurement/TestCases/tc-measurement-backend.md`):
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec). Identitas pengguna, menu, dan flag Guided Tooltip `guided_tooltip_seen_gs-measurement` (nilai true): disediakan tim FE.
  - Respons `POST /v2/enterprise-management/measurements/list`: 8 unit Pre-setup Client A (Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces), termasuk `Liter` / `L` dan `Gram` / `g`.
  - Respons `GET /v2/enterprise-management/measurements/{measurement_id}` bila halaman memanggilnya untuk mengisi form Edit: `Liter` / `L` dan `Gram` / `g`.
  - Respons `POST /v2/enterprise-management/measurements/check-availability`: nama tersedia untuk semua nilai Unit Name yang diketik.
  - Endpoint `PATCH /v2/enterprise-management/measurements/{measurement_id}` (Update Measurement) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: memakai unit Pre-setup `Liter` / `L` dan `Gram` / `g`; nilai Symbol `ltr` dan `gr` hanya diketik dan tidak pernah disimpan (pengecualian S-06: aksi dibatalkan atau dibuang lewat `[Leave]`, Last Updated tidak berubah). `Gram` adalah unit in-use FAMS yang hanya dibuka dan tidak diubah. Tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup.
- Kemampuan teknis: klik pada area backdrop di luar modal; penekanan Esc; deteksi muncul tidaknya dialog.
- State global: tidak ada yang diubah. Sesi berada di akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-86: Close Edit saat dirty lalu Cancel mempertahankan form

1. Klik `⋯` baris `Liter` > Edit
2. Ubah Symbol menjadi `ltr`
3. Tekan Esc
4. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
5. Klik [Cancel]
6. Verifikasi form Edit tetap terbuka
7. Verifikasi field Symbol berisi `ltr`

### TC-GS-UOM-87: Close Edit saat dirty lalu Leave membuang perubahan

8. Klik `[✕]` (melanjutkan form Edit `Liter` yang masih dirty dari langkah 2)
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik [Leave]
11. Verifikasi modal tertutup
12. Verifikasi Symbol `Liter` di tabel tetap `L`

### TC-GS-UOM-273: Klik backdrop saat form Edit dirty tidak menutup form

13. Klik `⋯` baris `Gram` > Edit
14. Ubah Symbol menjadi `gr`
15. Klik area backdrop di luar modal
16. Verifikasi form Edit tetap terbuka dengan Symbol `gr`
17. Verifikasi dialog `Unsaved Changes` tidak tampil
18. Klik icon `[✕]`
19. Verifikasi dialog `Unsaved Changes` tampil
20. Klik [Leave]
21. Verifikasi modal tertutup
22. Verifikasi Symbol `Gram` di tabel tetap `g`

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 22.
- TC-GS-UOM-87 melanjutkan form `Liter` yang masih dirty dari TC-GS-UOM-86 (langkah 8), bukan membuka form baru: kondisi awal TC-87 (Symbol `ltr`) sama dengan kondisi akhir TC-86. Jumlah pembukaan form (dua: `Liter` dan `Gram`) sama dengan jumlah kejadian menutup form (prinsip 6 konvensi).
- Langkah 4 mengasersi hanya judul dialog dan kedua tombol sesuai Expected TC-86 butir a; isi body dialog tidak diasersi karena TC tidak menyebutnya.
- Langkah 19 (`Verifikasi` dialog `Unsaved Changes` sebelum `[Leave]`) dari S-08; Expected TC-273 butir b hanya menyatakan dialog tidak tampil pada klik backdrop.
- Tidak ada pembagian TC lintas spec; seluruh TC sumber spec ini dikerjakan di sini.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert` karena gabungan keduanya 41 langkah (19 + 22), di atas batas sekitar 35 langkah; spec ini memakai form Edit yang sengaja dibiarkan dirty untuk menguji penutupan (Unsaved Changes, backdrop, Esc) pada `Liter` dan `Gram`, sedangkan 024 memakai form bersih dan form pasca-[Clear Field] (screening dan revert). Tiap spec membuka popup Edit sendiri sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA: daftar endpoint mock bersumber `tc-measurement-backend.md`; path dan skema endpoint disediakan tim FE sesuai `openapi.yaml` dan `low-level-design.md` modul (S-13).
