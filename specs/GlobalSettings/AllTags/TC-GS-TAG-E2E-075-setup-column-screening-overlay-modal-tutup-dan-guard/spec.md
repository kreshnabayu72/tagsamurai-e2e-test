---
id: TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard
title: "Setup Column Registri: Screening Column Visibility dan Modal, Tutup Tanpa Save, dan Guard Satu Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-227
  - TC-GS-TAG-228
  - TC-GS-TAG-237
  - TC-GS-TAG-238
coverage:
  web: automated
---

# Setup Column Registri: Screening Column Visibility dan Modal, Tutup Tanpa Save, dan Guard Satu Kolom

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata; keputusan D-3, pola File Manager).
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (respons yang dipaksa; endpoint dari `tc-all-tags-backend.md`, yang menyebut LLD dan OpenAPI modul; skema respons mengikuti openapi modul dan dilengkapi tahap script, S-13):
  - Daftar registri: `POST /v2/hardware-tagging/tags/list` (`tc-all-tags-backend.md` bagian 1). Mengembalikan 30 baris Seed Registri A (DD-01 sampai DD-30; 4 Paired dan 26 Not Paired; ukuran halaman 10) beserta kolom Last Scanned In, Activated At, dan Last User.
  - Kartu counter lisensi: `GET /v2/hardware-tagging/tags/license-counters` (bagian 2) dan kartu counter kesehatan: `GET /v2/hardware-tagging/tags/health-counters` (bagian 3), dipanggil halaman saat dibuka. Nilainya bebas dan tidak diasersi spec ini.
  - Opsi filter: `POST /v2/hardware-tagging/tags/options` (bagian 4), hanya bila halaman memuatnya saat dibuka. Tidak menjadi objek langkah spec ini.
  - Stream atau langganan real-time halaman TAG: tidak didefinisikan di sumber yang dibaca tahap ini (TC dan `tc-all-tags-backend.md`); bila halaman berlangganan, stream di-mock tanpa event dan disediakan tim FE (S-13).
  - Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-tag-registry`: true (di-mock). API pendukung di luar modul (identitas pengguna, sesi, menu, preferensi Guided Tooltip, General Settings) disediakan tim FE (S-13).
- Preferensi kolom (visibilitas, urutan, pin) diperlakukan sebagai pengaturan sisi klien yang tidak melewati API TAG; mekanisme penyimpanannya tidak didefinisikan di TC (lihat Temuan untuk QA), sehingga tidak ada endpoint yang di-mock untuknya.
- Suite serial (`parallel: false`): konfigurasi kolom adalah state global browser yang dipakai spec lain.
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`): pernyataan hook suite ada di `suite.md`; pada spec mock ini dipenuhi lewat respons preferensi Guided Tooltip yang di-mock true, sehingga walkthrough tidak muncul otomatis.
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom registri dikembalikan ke default (10 kolom Hideable tampil, 3 kolom Curated tersembunyi, urutan awal, tanpa pin).
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar, counter, dan opsi; mengarahkan kursor ke header kolom Actions dan ke checkbox disabled untuk membaca tooltip; menutup modal lewat `[✕]`.

## Test Steps

### TC-GS-TAG-227: Screening overlay Column Visibility

1. Arahkan kursor ke header kolom Actions (⋯)
2. Verifikasi tooltip `Column Visibility`
3. Klik header kolom Actions (⋯)
4. Verifikasi overlay memuat 13 kolom data berurutan `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned`, `Last Scanned In`, `Activated At`, `Last User`
5. Verifikasi setiap kolom pada overlay memiliki checkbox
6. Verifikasi setiap kolom pada overlay memiliki drag handle
7. Verifikasi checkbox `TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, dan `Last Scanned` tercentang
8. Verifikasi checkbox `Last Scanned In`, `Activated At`, dan `Last User` tidak tercentang
9. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
10. Verifikasi kolom Checkbox dan Actions tidak tercantum sebagai baris pada overlay

### TC-GS-TAG-228: Screening modal Setup Column dan Live Preview

11. Klik item `Setup Column...`
12. Verifikasi Zona 1: judul `Setup Column`
13. Verifikasi Zona 1: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
14. Verifikasi Zona 1: tombol `[✕]`
15. Verifikasi Zona 2: setiap kolom pada daftar memiliki checkbox
16. Verifikasi Zona 2: setiap kolom pada daftar memiliki drag handle
17. Verifikasi Zona 2: setiap kolom pada daftar memiliki ikon Pin
18. Verifikasi Zona 2: live preview menampilkan header kolom
19. Verifikasi Zona 2: live preview menampilkan data sel
20. Verifikasi Zona 3: tombol `Reset to Default` dan `Save`
21. Verifikasi tidak ada tombol `Cancel`
22. Klik `[✕]` untuk menutup modal

### TC-GS-TAG-237: Menutup modal tanpa Save membuang perubahan preview

23. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
24. Uncheck `Brand`
25. Klik `[✕]`
26. Verifikasi tabel kembali ke konfigurasi tersimpan terakhir
27. Verifikasi kolom `Brand` tetap tampil
28. Buka kembali modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
29. Klik `[✕]` untuk menutup modal

### TC-GS-TAG-238: Guard satu kolom tersisa

30. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
31. Uncheck `TAG Type`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, dan `Last Scanned` (sisakan `Code`)
32. Arahkan kursor ke checkbox `Code`
33. Verifikasi checkbox `Code` disabled dan tidak bisa di-uncheck
34. Verifikasi tooltip `At least one column must remain visible.`
35. Klik `[✕]` untuk menutup modal tanpa Save

## Notes

- Mode: mock. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (227, 228, 237, 238). Screening di awal, guard yang menonaktifkan checkbox di akhir; tidak ada aksi yang menyimpan konfigurasi atau menghapus data. TC-GS-TAG-229 sampai 232 dan 220 (hide, curated, reorder, persistensi, lintas tab) ada di spec `TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab`; TC-GS-TAG-233 sampai 236 (pin dan reset) ada di spec `TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default`.
- Panjang spec: 35 langkah, di bawah ambang sekitar 35 langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 22, 29, dan 35 (menutup modal tanpa Save).
- Langkah 28 (membuka kembali modal) adalah langkah TC-GS-TAG-237 yang tidak punya Expected sendiri; spec tidak menambah asersi untuk langkah itu.
- Temuan untuk QA:
  - Mekanisme penyimpanan preferensi kolom (sisi klien atau API) tidak didefinisikan di TC maupun `tc-all-tags-backend.md`; kutipan `prd-conventions.md` §9.3 yang dirujuk TC tidak menyebut endpoint. Spec mock mengasumsikan tidak ada endpoint dan tidak mengarang satu pun; bila persistensi ternyata lewat API, endpoint tambahan disediakan tim FE (S-13).
  - TC-GS-TAG-227 butir b menulis "13 kolom data" yang tercentang atau tidak dalam satu butir; spec memecahnya menjadi urutan, checkbox, drag handle, kelompok tercentang, dan kelompok tidak tercentang.
  - TC-GS-TAG-238 langkah 2 ("Uncheck seluruh kolom kecuali `Code`") tidak menyebut apakah kolom Curated yang default tersembunyi ikut dihitung; spec hanya meng-uncheck sembilan kolom Hideable yang tercentang.
  - Endpoint opsi dan stream (lihat Prerequisites) tidak berperan dalam langkah spec ini; kebutuhannya bergantung pada apa yang dipanggil halaman saat dibuka.
