---
id: TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert
title: "Screening Popup Edit Unit, Clear Field Tanpa Revert, dan Tutup Tanpa Perubahan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-69
  - TC-GS-UOM-84
  - TC-GS-UOM-85
coverage:
  web: automated
---

# Screening Popup Edit Unit, Clear Field Tanpa Revert, dan Tutup Tanpa Perubahan

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Edit Unit di browser.
- Kebutuhan mock (endpoint dari `global-settings/measurement/TestCases/tc-measurement-backend.md`):
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap. Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec). Identitas pengguna, menu, dan flag Guided Tooltip `guided_tooltip_seen_gs-measurement` (nilai true): disediakan tim FE.
  - Respons `POST /v2/enterprise-management/measurements/list`: 8 unit Pre-setup Client A (Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces), termasuk `Liter` dengan Symbol `L`.
  - Respons `GET /v2/enterprise-management/measurements/{measurement_id}` bila halaman memanggilnya untuk mengisi form Edit: `Liter` / `L`.
  - Respons `POST /v2/enterprise-management/measurements/check-availability` (cek keunikan Unit Name saat mengetik): nama tersedia untuk semua nilai yang diketik pada Unit Name.
  - Endpoint `PATCH /v2/enterprise-management/measurements/{measurement_id}` (Update Measurement) tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: memakai unit Pre-setup `Liter` / `L` (bebas relasi) hanya sebagai target buka Edit, tidak pernah disimpan (pengecualian S-06: aksi tanpa Save, Last Updated tidak berubah); tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup.
- Kemampuan teknis: pembacaan nilai field; deteksi muncul tidaknya dialog.
- State global: tidak ada yang diubah. Sesi berada di akun default suite (Total Control Client A), sehingga hook `after` tidak perlu memulihkan sesi.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).

## Test Steps

### TC-GS-UOM-69: Screening Popup Edit Unit

1. Klik `⋯` baris `Liter` > Edit
2. Verifikasi Header: Title `Edit Unit` dan icon `[✕]`
3. Verifikasi field `Unit Name *` terisi `Liter`
4. Verifikasi field `Symbol *` terisi `L`
5. Verifikasi checkbox `Stay on this form after submitting` tidak tampil
6. Verifikasi Footer: `[Clear Field]` dan `[Save]` (filled, success)
7. Verifikasi Footer tidak memuat `[Cancel]`

### TC-GS-UOM-85: Menutup form Edit tanpa perubahan tidak memunculkan dialog

8. Klik `[✕]` (tanpa mengubah apa pun pada popup Edit dari langkah 1)
9. Verifikasi modal tertutup
10. Verifikasi dialog Unsaved Changes tidak tampil

### TC-GS-UOM-84: Clear Field pada Edit mengosongkan field tanpa me-revert nilai tersimpan

11. Klik `⋯` baris `Liter` > Edit
12. Klik [Clear Field]
13. Verifikasi field `Unit Name *` kosong, bukan kembali ke `Liter`
14. Verifikasi field `Symbol *` kosong, bukan kembali ke `L`
15. Verifikasi dialog Unsaved Changes tidak tampil
16. Klik `[✕]`
17. Verifikasi dialog `Unsaved Changes` tampil
18. Klik [Leave]
19. Verifikasi baris `Liter` di tabel tetap menampilkan Unit Name `Liter` dan Symbol `L`

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 19.
- Urutan TC dalam spec: 69, 85, 84 (urutan sumber 69, 84, 85). Alasan: TC-69 dan TC-85 memakai popup Edit yang masih bersih sehingga berbagi satu pembukaan dan ditutup lewat `[✕]`; TC-84 membuka popup kedua, karena `[Clear Field]` membuat form tidak lagi bersih (prinsip 6 konvensi). Jumlah pembukaan sama dengan jumlah kejadian menutup form.
- Langkah penghubung: langkah 16 sampai 18 (menutup form yang dikosongkan lewat `[✕]` dan `[Leave]`, S-08) ditambahkan supaya Expected TC-84 butir c ("Data Liter di tabel tidak berubah") dapat diamati di langkah 19; TC tidak menyebut cara menutup form ini.
- Target `Liter` adalah baris Pre-setup yang hanya dibuka dan tidak pernah disimpan (pengecualian S-06). Pada TC sumber nama target juga `Liter`.
- Tidak ada pembagian TC lintas spec; seluruh TC sumber spec ini dikerjakan di sini.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog` karena gabungan keduanya 41 langkah (19 + 22), di atas batas sekitar 35 langkah; spec ini memakai form Edit `Liter` yang bersih lalu dikosongkan lewat `[Clear Field]` (screening dan revert), sedangkan 025 memakai form yang dibiarkan dirty untuk menguji penutupan (Unsaved Changes, backdrop, Esc) pada `Liter` dan `Gram`. Tiap spec membuka popup Edit sendiri sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-UOM-84 tidak menyebut apakah menutup form Edit yang sudah dikosongkan lewat `[Clear Field]` memunculkan dialog `Unsaved Changes`. Spec mengasumsikan form dianggap dirty (nilai berbeda dari nilai tersimpan) dan menutupnya lewat `[✕]` lalu `[Leave]`; perlu konfirmasi QA terhadap PRD.
  - Pencocokan endpoint mock memakai `tc-measurement-backend.md`; path dan skema endpoint pendukung halaman (mis. `GET` detail untuk mengisi form Edit) disediakan tim FE sesuai `openapi.yaml` dan `low-level-design.md` modul (S-13).
