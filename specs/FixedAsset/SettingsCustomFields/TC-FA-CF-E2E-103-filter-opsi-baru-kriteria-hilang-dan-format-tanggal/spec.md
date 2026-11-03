---
id: TC-FA-CF-E2E-103-filter-opsi-baru-kriteria-hilang-dan-format-tanggal
title: "Filter: Opsi Baru Setelah Create, Kriteria Hilang, dan Format Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-639
  - TC-FA-CF-642
  - TC-FA-CF-643
coverage:
  web: automated
---

# Filter: Opsi Baru Setelah Create, Kriteria Hilang, dan Format Tanggal

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Sesi API aktor (Pre-setup #28, pelaku kedua yang hanya memicu perubahan state): login API (password `Spectra.env.FA_TC_PASSWORD`) untuk akun yang sama dengan sesi UI, memakai token yang tidak dihitung sebagai sesi web (dinyatakan di `suite.md`; kemampuan disediakan tim BE/FE). Sesi ini dipakai pada langkah 15.
- Data Pre-setup (bernama literal tanpa suffix karena asersi bergantung pada nama baris; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), baseline tab General (Pre-setup #12) delapan field: `Asset Serial Tag` (Text), `Storage Capacity` (Numeric), `Equipment Class` (Dropdown), `Operating Voltage` (Text), `Total Cost` (Formula), `Depreciated Ratio` (Percentage, satu-satunya field Percentage), `Compliance File` (Document), `Legacy Tag` (Text). Baseline tab General tidak memiliki Data Type `Email`.
- Data Pre-setup yang diubah spec ini: `Depreciated Ratio` dihapus lewat sesi API pada langkah 15 (kuota satu-satunya field Percentage tidak dapat dimiliki spec; S-06 pengecualian). Pemulihan ke keadaan awal dijamin seed reset baseline Company Alpha (fixture backend, kemampuan disediakan tim FE/BE, dinyatakan di `suite.md`) di hook `before` dan `after`. Efek: Last Updated dan entri audit trail (Changelog, Activity Log, System Log) field itu berubah; suite berjalan serial.
- Pengaturan (Pre-setup #27): General Settings Company Alpha varian Date Format `dd MMM yy`, Time Format 12 jam, Time Zone `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`, disiapkan lewat seed di hook `before` spec ini dan dipulihkan ke baseline (`dd/MM/yy`, 24 jam, `(UTC+07:00) Bangkok, Hanoi, Jakarta`) di hook `after`.
- Data Dinamis milik spec: `New Email Field {runId}-103` (Email), dibuat lewat UI pada langkah 6 sampai 9; dihapus lewat API di hook `after`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `New Email Field {runId}-103` lewat API, pulihkan `Depreciated Ratio` lewat seed reset baseline, pulihkan General Settings ke baseline.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan teks tanggal pada input Last Updated, opsi dropdown filter, nilai field filter, serta toast dan pesan inline.
- State global: General Settings Date Format dan Time Zone (varian Pre-setup #27) dan penghapusan `Depreciated Ratio`, dipulihkan sebagaimana di atas.

## Test Steps

### TC-FA-CF-643: Input Date Filter tabel utama mengikuti Date Format General Settings varian

1. Klik ikon Filter
2. Pilih Last Updated 13 Oct 26 sampai 16 Oct 26, klik `[Apply]`
3. Verifikasi input Last Updated menampilkan teks tanggal terpilih dalam format `dd MMM yy` (`13 Oct 26` sampai `16 Oct 26`)

### TC-FA-CF-639: Opsi dropdown filter Data Type memuat tipe baru setelah Create tanpa reload

4. Klik `[Clear Field]`, klik `[Apply]`
5. Klik ikon Filter untuk menutup Filter Panel
6. Klik `[+ Custom Field]`
7. Isi Field Name `New Email Field {runId}-103`, pilih Data Type `Email`
8. Klik `[Submit]`
9. Tunggu aksi selesai (modal Create tertutup)
10. Klik ikon Filter
11. Buka dropdown Data Type
12. Verifikasi dropdown Data Type memuat `Email` tanpa memuat ulang halaman

### TC-FA-CF-642: Kriteria filter yang sudah tidak ada dibersihkan saat filter diterapkan ulang

13. Pilih Data Type `Percentage`, klik `[Apply]`
14. Tunggu aksi selesai (tabel menampilkan hasil filter Percentage)
15. Hapus `Depreciated Ratio` lewat sesi API aktor hingga tersimpan
16. Klik ikon Filter untuk menutup Filter Panel
17. Klik ikon Filter untuk membuka Filter Panel
18. Klik `[Apply]`
19. Verifikasi nilai `Percentage` dibersihkan dari kriteria (field filter `Data Type` tidak lagi berisi `Percentage`)
20. Verifikasi tabel tidak lagi disaring Data Type (baris `Asset Serial Tag` bertipe `Text` dan `Storage Capacity` bertipe `Numeric` tampil bersamaan)
21. Verifikasi tidak ada pesan error (tidak ada toast error dan tidak ada pesan inline)

## Notes

- Spec memuat 21 langkah, di bawah ambang sekitar 35 langkah. Satu topik (perilaku Filter Panel terhadap perubahan data dan format), satu akun, satu dataset Company Alpha.
- Urutan TC berbeda dari urutan TC sumber (TC-FA-CF-643 lebih dulu, lalu TC-FA-CF-639, lalu TC-FA-CF-642): TC-FA-CF-642 menghapus data Pre-setup sehingga ditaruh paling akhir (S-10). Varian General Settings Pre-setup #27 berlaku untuk seluruh spec dan tidak memengaruhi asersi TC-FA-CF-639 dan TC-FA-CF-642.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (`[Clear Field]` melepas filter tanggal) dan 5 (menutup Filter Panel); langkah 9 dan 14 ("Tunggu aksi selesai" sesudah aksi tanpa asersi sebelum pindah surface atau sesi, bagian 8b butir 8); langkah 16 dan 17 (menutup dan membuka kembali Filter Panel mengikuti langkah TC-FA-CF-642 "Buka Filter Panel dan klik `[Apply]` lagi").
- Langkah pemicu pelaku kedua (langkah 15) lewat sesi API aktor ditulis "... hingga ... tersimpan" (R-20); tidak memakai butir `P-2` karena bukan konteks UI kedua.
- Langkah 21 (tidak ada pesan error) ditaruh sesudah langkah 20 supaya tabel yang tampil menjadi anchor positif sebelum asersi absence (bagian 8b butir 2); Expected a TC-FA-CF-642 menyebut "tanpa pesan error" dalam kalimat yang sama dengan pembersihan kriteria.
- Temuan untuk QA:
  - TC-FA-CF-642 menyebut "Dari sesi lain hapus `Depreciated Ratio`" tanpa menyebut mekanisme sesi; Pre-setup #28 menyebut dua sesi Total Control (#1 dan #10) dan spec memakai sesi API untuk akun yang sama dengan sesi UI.
  - TC-FA-CF-642 menandai Automation `Manual Only — (d) dua sesi paralel`; spec tetap ditulis karena pelaku kedua hanya memicu perubahan state lewat sesi API.
  - TC-FA-CF-642 Expected b menyebut "hasil sesuai kriteria tersisa" tanpa nama baris; langkah 20 mengasersi dua baris dengan Data Type berbeda tampil bersamaan.
  - TC-FA-CF-642 tidak menyebut apakah pesan "tanpa pesan error" mencakup toast atau pesan inline; langkah 21 mencakup keduanya.
  - TC-FA-CF-639 tidak menyebut Scope atau nilai field wajib lain pada Create; spec hanya mengisi Field Name dan Data Type (nilai bawaan form Create dipakai).
  - TC-FA-CF-643 tidak menyebut tampilan teks rentang pada input (pemisah antara dua tanggal); langkah 3 mengasersi kedua tanggal dalam format `dd MMM yy`.
  - TC-FA-CF-639, TC-FA-CF-642, dan TC-FA-CF-643 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
