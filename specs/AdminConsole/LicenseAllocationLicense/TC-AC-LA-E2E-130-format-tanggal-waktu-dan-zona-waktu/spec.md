---
id: TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu
title: "Format Tanggal, Waktu, dan Zona Waktu per Surface Mengikuti General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-420
  - TC-AC-LA-421
  - TC-AC-LA-422
  - TC-AC-LA-424
  - TC-AC-LA-382
coverage:
  web: automated
---

# Format Tanggal, Waktu, dan Zona Waktu per Surface Mengikuti General Settings

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Hendra Wijaya; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Hendra Wijaya | #1 | Total Control Principal | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: seed 30 alokasi lintas status dan 25 entri Changelog (Pre-setup #54, hanya dibaca); alokasi dengan riwayat log lengkap (Pre-setup #55, hanya dibaca): `{idLog}` (entri Allocation Log dan Changelog) dan `{idTz}` (entri tersimpan `03:00 UTC`, ditetapkan fixture).
- General Settings awal (disetel hook `before`): Date Format `dd MMM yy`, Time Format 24 jam, zona waktu Asia/Jakarta (UTC+07:00).
- Kemampuan teknis (disediakan tim FE/BE; TC tidak menyebut halaman maupun akun pengubah General Settings): kemampuan mengubah General Settings (Date Format, Time Format) dan memulihkannya; penetapan waktu simpan entri `{idTz}` ke `03:00 UTC`.
- State global: General Settings diubah dua kali (Time Format 12 jam, lalu Date Format `dd/MM/yy`) dan dipulihkan ke nilai awal di hook `after`; Last Updated dan entri audit trail General Settings berubah dan dicatat sebagai efek S-06.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Surface 2: Modal Changelog (TC-AC-LA-421)

1. Klik ikon `Changelog` pada List
2. Verifikasi kolom Date memakai Date Format `dd MMM yy` dan Time Format 24 jam sesuai General Settings aktif
3. Pilih rentang tanggal pada filter Date
4. Verifikasi input date picker memakai konfigurasi General Settings aktif
5. Tutup modal Changelog

### Surface 3: Allocation Log (TC-AC-LA-422)

6. Ketik Search `{idLog}`, tekan Enter
7. Klik row action `Allocation Log` pada baris `{idLog}`
8. Verifikasi Date & Time tiap entri memakai Date Format `dd MMM yy` dan Time Format 24 jam General Settings
9. Tutup modal Allocation Log

### Zona waktu (TC-AC-LA-424)

10. Ganti isi kotak search dengan `{idTz}`, tekan Enter
11. Verifikasi Last Updated baris `{idTz}` pada List tampil `10:00` (UTC+07:00)
12. Klik ikon `Changelog` pada List
13. Ketik Search `{idTz}`, tekan Enter
14. Verifikasi Date entri `{idTz}` pada Changelog tampil `10:00` (UTC+07:00)
15. Tutup modal Changelog

### Surface 1: Last Updated dan filter List, konfigurasi awal (TC-AC-LA-420 butir a)

16. Klik `(←)` pada kotak Search
17. Verifikasi kolom Last Updated memakai Date Format `dd MMM yy`, Time Format 24 jam, dan zona waktu Asia/Jakarta
18. Pilih rentang tanggal pada filter Last Updated
19. Verifikasi teks input date picker memakai Date Format `dd MMM yy`, Time Format 24 jam, dan zona waktu Asia/Jakarta

### Changelog setelah Time Format diubah ke 12 jam (TC-AC-LA-382)

20. Ubah Time Format General Settings menjadi 12 jam (Date Format tetap `dd MMM yy`)
21. Tunggu aksi selesai (Time Format 12 jam tersimpan)
22. Klik ikon `Changelog` pada List
23. Verifikasi kolom Date memakai Date Format `dd MMM yy` dan Time Format 12 jam sesuai konfigurasi aktif
24. Tutup modal Changelog

### Surface 1: Last Updated dan filter List, konfigurasi baru (TC-AC-LA-420 butir b)

25. Ubah Date Format General Settings menjadi `dd/MM/yy` (Time Format tetap 12 jam)
26. Tunggu aksi selesai (Date Format `dd/MM/yy` tersimpan)
27. Muat ulang halaman
28. Verifikasi kolom Last Updated memakai Date Format `dd/MM/yy` dan Time Format 12 jam
29. Pilih rentang tanggal pada filter Last Updated
30. Verifikasi teks input date picker memakai Date Format `dd/MM/yy` dan Time Format 12 jam

## Notes

- Urutan blok berbeda dari urutan sourceTc agar General Settings hanya diubah dua kali: konfigurasi awal dipakai untuk TC-AC-LA-421, 422, 424, dan TC-AC-LA-420 butir a; Time Format 12 jam untuk TC-AC-LA-382; Date Format `dd/MM/yy` untuk TC-AC-LA-420 butir b. TC-AC-LA-382 langkah 1 ("Buka Changelog dan amati kolom Date") sama dengan langkah 2 pada konfigurasi awal.
- Langkah penghubung (S-03, R-16): langkah 6, 10, dan 13 (Search baris atau entri berdasarkan Allocation ID), langkah 16 (mengosongkan Search dengan `(←)`), langkah 5, 9, 15, dan 24 (menutup modal), langkah 20 dan 25 (mengubah General Settings), langkah 27 (muat ulang), langkah 21 dan 26 (menunggu aksi selesai karena langkah berikutnya membuka surface lain atau memuat ulang, 8b butir 8).
- Temuan untuk QA:
  - TC-AC-LA-420 sampai 424 dan 382 tidak menyebut halaman, akun, maupun mekanisme pengubahan General Settings; spec memakai kemampuan "disediakan tim FE/BE".
  - TC-AC-LA-420 butir a tidak menyebut contoh nilai tampil; spec mengasersi format konfigurasi aktif tanpa nilai literal. TC-AC-LA-420 langkah 3 mengubah Date Format dan 12 jam sekaligus, sedangkan TC-AC-LA-382 mengubah hanya Time Format; spec memisahkannya menjadi dua perubahan berurutan.
  - TC-AC-LA-424 menyebut "entri tersimpan 03:00 UTC" pada record Pre-setup #55 tanpa menyebut cara menetapkannya; spec memakai penetapan lewat fixture yang disediakan tim FE/BE. TC-AC-LA-424 menyebut jam `10:00` tanpa tanggal.
  - TC-AC-LA-422 dan TC-AC-LA-424 tidak menyebut record Pre-setup #55 yang dipakai; spec memakai `{idLog}` dan `{idTz}`.
  - TC-AC-LA-420 butir a menyebut Time Format 24 jam dan zona waktu pada teks input date picker; TC tidak menyebut bahwa picker menampilkan jam.
