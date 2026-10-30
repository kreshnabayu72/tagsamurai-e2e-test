---
id: TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog
title: "Resilience Download: Toast Error saat Unduh Tabel Utama dan Modal Changelog Gagal karena 5xx atau Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-251
  - TC-GS-UCF-552
  - TC-GS-UCF-273
  - TC-GS-UCF-553
coverage:
  web: automated
---

# Resilience Download: Toast Error saat Unduh Tabel Utama dan Modal Changelog Gagal karena 5xx atau Timeout

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Respons yang dipaksa:
  - Daftar Custom Field (`POST /v2/iam/user-custom-fields/list`; openapi.yaml:13, low-level-design.md:15): memuat 14 Custom Field Client A, yaitu Pre-setup `Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date` dan Population `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number` (nama literal karena isi respons mock, tanpa backend nyata).
  - Request export tabel utama (opsi CSV; `POST /v2/iam/user-custom-fields/export`; openapi.yaml:146, low-level-design.md:148): respons 500 (langkah 1); koneksi diputus sehingga request tidak sampai ke server (langkah 8).
  - Daftar entri Changelog Custom Field (`POST /v2/activity-logs/changelogs/list` dengan `logTable: "Custom Field"` dan `product: "global_settings"`; layanan activity-log, low-level-design.md:7; tidak ada di openapi.yaml modul): memuat 8 entri Pre-setup (Edit `Cost Center`, Create `Cost Center`, Activate `Employee Grade`, Deactivate `Joining Date`, Delete `Legacy Field`, Create `Job Description`, Create `Bonus`, Create `Office Phone`) dan 8 entri Create Population.
  - Request export Changelog (opsi CSV; tidak ada di openapi.yaml maupun low-level-design.md modul, disediakan tim FE): respons 500 (langkah 17); koneksi diputus sehingga request tidak sampai ke server (langkah 24).
  - Opsi Filter (`POST /v2/iam/user-custom-fields/options`; openapi.yaml:89, low-level-design.md:93). Stream SSE bila halaman berlangganan tidak ada di openapi.yaml maupun low-level-design.md modul; disediakan tim FE bila diperlukan.
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar ikon Download dan ikon Changelog tampil, flag Guided Tooltip) disediakan tim FE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis: tidak ada yang dibuat di backend; data tabel dan entri Changelog hanya isi respons mock dan dipakai sebagai precondition TC, tidak diasersi langkah. Fixture baru `Fixture.customFieldUser.resilienceDownload060`.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini, pulihkan koneksi jaringan, dan tutup Modal Changelog bila masih terbuka.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request export dan untuk memutus koneksi (request export tidak sampai ke server); memantau event unduhan browser (untuk memastikan tidak ada berkas terunduh); pembacaan toast error beserta ada tidaknya tombol `[Try Again]`; men-dismiss toast.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`); pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.

## Test Steps

### TC-GS-UCF-251: Download tabel utama gagal menampilkan toast error

1. Pasang intercept pada request export tabel utama: respons 500
2. Klik Download > `Download as CSV`
3. Verifikasi toast error "Error, failed to download Custom-Field-User-List." tampil
4. Verifikasi tidak ada berkas terunduh
5. Verifikasi tabel tetap tampil
6. Dismiss toast error
7. Lepas intercept pada request export tabel utama

### TC-GS-UCF-552: Download tabel utama timeout menampilkan toast gagal tanpa tombol Try Again

8. Putuskan koneksi jaringan sehingga request export tabel utama tidak sampai ke server
9. Klik Download > `Download as CSV`
10. Verifikasi toast error "Error, failed to download Custom-Field-User-List." tampil
11. Verifikasi toast error tidak memiliki tombol `[Try Again]`
12. Verifikasi tidak ada berkas terunduh
13. Verifikasi tabel tetap tampil
14. Dismiss toast error
15. Pulihkan koneksi jaringan

### TC-GS-UCF-273: Download Changelog gagal menampilkan toast error

16. Klik icon Changelog
17. Paksa respons export Changelog 500 lewat intercept
18. Klik Download > `Download as CSV`
19. Verifikasi toast error "Error, failed to download Changelog-Custom-Field." tampil
20. Dismiss toast error
21. Lepas intercept pada request export Changelog
22. Klik `✕` di header untuk menutup Modal Changelog

### TC-GS-UCF-553: Download Changelog timeout menampilkan toast gagal tanpa tombol Try Again

23. Klik icon Changelog
24. Putuskan koneksi jaringan sehingga request export Changelog tidak sampai ke server
25. Klik Download > `Download as CSV`
26. Verifikasi toast error "Error, failed to download Changelog-Custom-Field." tampil
27. Verifikasi toast error tidak memiliki tombol `[Try Again]`
28. Verifikasi tidak ada berkas terunduh
29. Verifikasi Modal Changelog tetap tampil
30. Dismiss toast error
31. Pulihkan koneksi jaringan
32. Klik `✕` di header untuk menutup Modal Changelog

## Notes

- Mode: mock. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Asersi yang menyangkut state backend nyata tidak teruji pada mode mock: spec ini hanya mengasersi tampilan toast, ada tidaknya tombol `[Try Again]`, tidak adanya berkas terunduh, dan tampilan tabel atau Modal Changelog dari respons mock. Post Condition keempat TC kosong ("-").
- Langkah penghubung (aksi tanpa `Verifikasi`): pasang dan lepas intercept, putuskan dan pulihkan koneksi jaringan, dismiss toast error (toast error tidak hilang otomatis dan didismiss sebelum TC berikutnya, S-09), klik icon Changelog yang membuka Modal Changelog pada TC-GS-UCF-273 dan 553, dan klik `✕` yang menutup Modal Changelog (tidak ada form dirty sehingga tidak ada dialog).
- Verifikasi "tidak ada berkas terunduh" pada TC-GS-UCF-273 tidak ada karena Expected TC-GS-UCF-273 hanya memuat toast; TC-GS-UCF-553 memuatnya pada Expected b.
- Pembagian TC lintas spec: Download tabel utama pada kondisi normal (TC-GS-UCF-244 sampai 250, 252) ada di spec 057; Download di atas 5.000 baris (TC-GS-UCF-365) di spec 058; Download Modal Changelog pada kondisi normal (TC-GS-UCF-272, 530 sampai 532) di spec 066.
- Temuan untuk QA:
  - Keputusan user: spec resilience memakai `Mode: mock`. TC-GS-UCF-251 dan TC-GS-UCF-552 mengasersi "tabel tetap tampil" dan TC-GS-UCF-553 "Modal Changelog tetap tampil" yang terbaca dari respons mock; tidak ada Expected yang mengasersi state backend.
  - TC-GS-UCF-552 dan TC-GS-UCF-553 menulis "Putuskan koneksi jaringan" tanpa durasi timeout; spec memutus koneksi lewat intercept pada request export dan tidak menyebut durasi (disediakan tim FE).
  - TC-GS-UCF-273 dan 553 menyebut nama berkas pada toast "Changelog-Custom-Field", sedangkan toast tabel utama memakai "Custom-Field-User-List"; teks toast mengikuti TC (tidak diverifikasi ke `toast-copy.md` pada tugas ini).
  - TC-GS-UCF-251 dan 273 menulis "Paksa respons export ... 500" tanpa path endpoint; endpoint export tabel utama dirujuk `POST /v2/iam/user-custom-fields/export` (openapi.yaml:146, LLD:148); list Changelog `POST /v2/activity-logs/changelogs/list` (LLD:7); export Changelog tidak ada di API modul dan disediakan tim FE.
  - TC-GS-UCF-273 dan 553 memuat 8 entri Create Population pada Changelog; entri itu hanya isi respons mock dan tidak diasersi.
