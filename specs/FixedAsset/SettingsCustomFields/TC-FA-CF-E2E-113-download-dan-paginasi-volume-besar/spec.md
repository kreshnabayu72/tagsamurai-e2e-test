---
id: TC-FA-CF-E2E-113-download-dan-paginasi-volume-besar
title: "Download pada Volume Besar: 120 Baris, 5.001 Baris, dan 5.001 Entri Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-419
  - TC-FA-CF-433
  - TC-FA-CF-479
coverage:
  web: automated
---

# Download pada Volume Besar: 120 Baris, 5.001 Baris, dan 5.001 Entri Changelog

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`). Kelas harness: volume data (satu jenis harness; tiga dataset dipakai berurutan, masing-masing satu Company).
- Akun aktor pertama: Total Control Company Volume (Pre-setup #20) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Volume (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_VOLUME_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun kedua (langkah 5 dan 6, Ganti akun untuk TC-FA-CF-433): Total Control Company Export (Pre-setup #21), email mengikuti pola yang sama dengan `{namaCompany}` = Company Export, `Spectra.env.FA_TC_EXPORT_PASSWORD`.
- Akun ketiga (langkah 13 dan 14, Ganti akun untuk TC-FA-CF-479): Total Control Company Log Volume (Pre-setup #19, varian 5.001 entri), email mengikuti pola yang sama dengan `{namaCompany}` = Company Log Volume, `Spectra.env.FA_TC_LOGVOLUME_PASSWORD`.
- Nama env `FA_TC_VOLUME_PASSWORD`, `FA_TC_EXPORT_PASSWORD`, dan `FA_TC_LOGVOLUME_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini; seed volume disediakan tim FE/BE dan dipulihkan hook `before`): Company Volume dengan 120 field Inactive pada tab General (`Volume Field 001` sampai `Volume Field 120`), fixture baru `Fixture.faCustomFields.volume`; Company Export dengan 5.001 field Inactive pada tab General dan Master Data Count Limit minimal 5.001, fixture baru `Fixture.faCustomFields.export`; Company Log Volume dengan 5.001 entri Changelog pada tab General, fixture baru `Fixture.faCustomFields.logVolume` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: penangkapan berkas unduhan dan pembacaan nama berkas serta jumlah baris data CSV; pembacaan jumlah entri Changelog tab General Company Log Volume sebelum aksi (N, langkah 15; audit trail tidak diasersi sebagai angka absolut, bagian 8b butir 10); pengamatan loading screen; pembacaan ada tidaknya job latar ekspor (disediakan tim FE/BE, TC tidak menyebut caranya, lihat Temuan untuk QA).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CF-419: Download tanpa Search atau Filter mengekspor seluruh baris tab aktif lintas halaman (Company Volume)

1. Klik icon Download > `Download as CSV`
2. Verifikasi tidak ada toast sukses
3. Verifikasi berkas `Custom-Fields.csv` terunduh
4. Verifikasi berkas memuat seluruh 120 baris tab General (bukan hanya 10 baris halaman aktif)

### TC-FA-CF-433: Download di atas 5.000 baris memakai loading screen tanpa job background (Company Export)

5. Ganti akun: Logout dari akun Total Control Company Volume
6. Login sebagai Total Control Company Export (Pre-setup #21) dengan `Spectra.env.FA_TC_EXPORT_PASSWORD`
7. Buka Fixed Asset > Settings > Custom Fields lewat menu sidebar
8. Klik icon Download > `Download as CSV`
9. Verifikasi loading screen tampil sampai berkas siap
10. Verifikasi tidak ada toast informasional, notifikasi in-app, atau job background
11. Verifikasi berkas langsung terunduh
12. Verifikasi berkas memuat seluruh 5.001 baris

### TC-FA-CF-479: Download Modal Changelog dengan di atas 5.000 entri (Company Log Volume)

13. Ganti akun: Logout dari akun Total Control Company Export
14. Login sebagai Total Control Company Log Volume (Pre-setup #19, varian 5.001 entri) dengan `Spectra.env.FA_TC_LOGVOLUME_PASSWORD`
15. Buka Fixed Asset > Settings > Custom Fields lewat menu sidebar, lalu catat jumlah entri Changelog tab General (N)
16. Klik icon Changelog
17. Klik icon Download > `Download as CSV`
18. Verifikasi loading screen tampil
19. Verifikasi tidak ada notifikasi in-app
20. Verifikasi berkas terunduh
21. Verifikasi berkas memuat seluruh entri (N baris data)

## Notes

- Spec memuat 21 langkah, di bawah ambang sekitar 35 langkah. Satu kelas harness (volume data) dan satu topik (Download di atas batas lazim), dengan tiga dataset yang dipakai berurutan dan saling bebas.
- Urutan TC di spec: 419, 433, 479. Dataset dibangun dari yang terkecil ke terbesar; akun aktor pertama dan hook `before` adalah Total Control Company Volume sehingga TC pertama tidak butuh ganti akun (S-07). Langkah 5 dan 6, 13 dan 14 adalah Ganti akun eksplisit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 15 (membuka halaman setelah ganti akun; langkah 15 juga mencatat N), langkah 16 (membuka Modal Changelog sesuai langkah uji TC-FA-CF-479). Langkah 10 dan 19 (absence state sementara) ditulis tepat setelah pemicu dan sebelum asersi berkas (bagian 8b butir 11); loading screen pada langkah 9 dan 18 diasersi sebelum langkah berikut yang mengubah state itu (bagian 8b butir 5).
- Pembagian ke Company mengikuti Precondition masing-masing TC (Pre-setup #20, #21, dan #19 varian 5.001 entri).
- Temuan untuk QA:
  - Email akun Total Control Company Volume, Export, dan Log Volume tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-479 Judul/Skenario menyebut "Paginasi dan Download", tetapi Langkah Uji dan Expected hanya memuat Download; paginasi tidak diasersi di spec ini. Data Uji merujuk "Pre-setup #19b" yang tidak ada (varian 5.001 entri ada di baris Pre-setup #19).
  - TC-FA-CF-479 Expected "berkas memuat seluruh entri" tidak menyebut angka; karena audit trail tidak boleh diasersi sebagai angka absolut (S-12), spec membandingkan dengan N yang dibaca sebelum aksi (langkah 15).
  - TC-FA-CF-433 Expected b ("tidak ada ... job background") tidak menyatakan cara mengamati job latar; spec memakai kemampuan baca yang disediakan tim FE/BE, tanpa mengarang endpoint.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
