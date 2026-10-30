---
id: TC-GS-TAG-E2E-015-mobile-registri-tanpa-bulk-activate-gps-manual-dan-visibilitas
title: "Mobile: Tanpa Bulk Delete/Resolve/Remove, Activate GPS Hanya Entri Manual, dan Visibilitas Tombol per Tab dan Role"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-332
  - TC-GS-TAG-333
  - TC-GS-TAG-334
coverage:
  mobile: automated
---

# Mobile: Tanpa Bulk Delete/Resolve/Remove, Activate GPS Hanya Entri Manual, dan Visibilitas Tombol per Tab dan Role

## Prerequisites

- Mode: FE+BE (mobile). Platform: aplikasi native Android TAG Samurai Mobile; registri tampil sebagai kartu dengan menu `[⋯]` dan toolbar.
- Perangkat atau emulator Android dengan aplikasi terpasang, kemampuan mengetuk, menekan lama, dan membaca elemen UI. Perangkat fisik bersama: `parallel: false` (S-09).
- Kemampuan teknis (disediakan tim FE): kontrol navigasi aplikasi untuk keluar dari halaman Activate TAG di mobile (langkah 15 dan 20); kontrol ini tidak didefinisikan di TC maupun PRD.
- Login akun aktor pertama (Total Control) di aplikasi Android pada hook `before`; ganti akun ke Read Only ditulis sebagai langkah. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.

Akun yang diuji (Tabel Data Uji Pre-setup; Client A):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-332, TC-333 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-334 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |

- Data Pre-setup (hanya dibaca): Seed Registri A (DD-02 `E2801160600002054D8A0002` Available dipakai sebagai kartu target); IMEI `356938035643101` dan `356938035643102` (DD-N1, DD-N2; GPS tidak ada di stok, menjadi baris Needs Info) untuk TC-332. Spec tidak menyimpan perubahan; sesi Activate ditutup tanpa Submit. Seed di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Layar awal: registri TAG di aplikasi Android dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, registri dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` disetel true untuk kedua akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: layar mobile belum punya ID/aria-label di sumber (PRD hanya menetapkan target Guided Tooltip); diselesaikan tim FE di tahap script.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-332: Mobile: Bulk Delete, Bulk Resolve, dan Bulk Remove tidak tersedia; Delete per tag lewat menu kartu

1. Buka Tab Not Paired di registri mobile
2. Tekan lama kartu DD-02
3. Verifikasi tekan lama tidak masuk selection mode
4. Verifikasi tidak ada kolom checkbox
5. Verifikasi tidak ada bar bulk
6. Buka menu `[⋯]` kartu DD-02
7. Verifikasi menu `[⋯]` kartu memuat `TAG Log` dan `Delete` dengan gating yang sama seperti web
8. Tutup menu `[⋯]`
9. Buka Activate TAG tipe GPS
10. Ketik `356938035643101` di input entri manual, klik `Add`
11. Ketik `356938035643102` di input entri manual, klik `Add`
12. Verifikasi kedua baris berstatus Needs Info di staging
13. Verifikasi tidak ada opsi Bulk Resolve pada staging
14. Verifikasi tidak ada opsi Remove massal pada staging
15. Tutup halaman Activate lewat kontrol navigasi aplikasi (disediakan tim FE), lalu klik `[Leave]` pada dialog `Unsaved Changes`

### TC-GS-TAG-333: Mobile: Activate GPS hanya lewat entri manual (tanpa unggah berkas)

16. Buka Activate TAG tipe GPS
17. Amati kontrol masuk data
18. Verifikasi tidak ada kontrol unggah berkas CSV/XLSX
19. Verifikasi entri manual IMEI tersedia
20. Tutup halaman Activate lewat kontrol navigasi aplikasi (disediakan tim FE); form bersih sehingga tidak ada dialog

### TC-GS-TAG-334: Mobile: visibilitas tombol per tab dan role identik dengan web

21. Logout, lalu login sebagai Read Only (Maya Putri) di aplikasi Android
22. Buka registri TAG di Tab All
23. Amati header dan menu `[⋯]` toolbar
24. Verifikasi menu `[⋯]` toolbar memuat `Filter` dan `Download`
25. Verifikasi `Audit TAG` Hidden
26. Verifikasi `Delete by Scan` Hidden
27. Verifikasi `+ Activate TAG` Hidden
28. Verifikasi `Event Log` tampil di Tab All
29. Klik Tab Paired
30. Amati header
31. Verifikasi `Event Log` Hidden di Tab Paired
32. Verifikasi kartu Status tidak tampil di Tab Paired

## Notes

- Mode: FE+BE (mobile). Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 10). TC-332 sampai 334 berlabel `Manual Only — (b)` (perangkat dan aplikasi native Android); tetap masuk spec (D-4).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 6, 8, 9, 16, 22 sampai 23, 30 (membuka dan mengamati), langkah 15 dan 20 (keluar dari halaman Activate lewat kontrol navigasi aplikasi; langkah 15 memakai `[Leave]` karena form dirty, langkah 20 tanpa dialog karena form bersih, S-08), langkah 21 (ganti akun eksplisit, S-07). Langkah 24 adalah anchor positif untuk absence tombol Hidden (langkah 25 sampai 27); langkah 28 adalah anchor untuk langkah 31 (8b butir 2) dan memverifikasi bahwa `Event Log` tampil di Tab All untuk Read Only (konsisten dengan TC-27, spec 006); asersi ini tidak ada di TC-334 dan dicatat sebagai anchor. Langkah 12 (`Verifikasi` kedua baris berstatus Needs Info) tidak ada di Expected TC-332; dipakai sebagai anchor positif untuk absence opsi Bulk Resolve dan Remove massal pada langkah 13 dan 14 (S-03, 8b butir 2).
- Penyimpangan urutan: TC-332 langkah 3 (Activate dengan dua baris Needs Info) ditaruh setelah pengujian kartu karena menutup halaman dirty; TC-333 ditaruh setelah TC-332 pada akun yang sama; TC-334 terakhir karena ganti akun.
- Temuan untuk QA:
  - TC-332 butir b ("gating yang sama seperti web") tidak menyebut isi menu untuk baris Paired maupun role lain; spec mengasersi `TAG Log` dan `Delete` pada kartu DD-02 (Available) untuk Total Control.
  - TC-332 langkah 3 tidak menyebut IMEI Needs Info yang dipakai; spec memakai DD-N1 dan DD-N2 (GPS tidak ada di stok).
  - TC-332 dan TC-333 tidak menyebut cara menutup halaman Activate di mobile; spec memakai kontrol navigasi aplikasi yang disediakan tim FE (kontrol mobile belum didefinisikan di TC maupun PRD) dan `[Leave]` pada dialog `Unsaved Changes` bila form dirty.
  - TC-334 Expected menyebut "kartu Status" tanpa definisi (kartu counter lisensi/kesehatan atau kartu Status per tag); spec mengikuti teks TC.
  - TC-334 menyebut `[⋯]` toolbar tanpa daftar isi lengkap; PRD §4.6 menyebut `Filter`, `Download`, `Audit TAG`, `Delete by Scan` (ketika diizinkan); spec memakai `Filter` dan `Download` sebagai anchor.
  - Post Condition semua TC bernilai `-`.
