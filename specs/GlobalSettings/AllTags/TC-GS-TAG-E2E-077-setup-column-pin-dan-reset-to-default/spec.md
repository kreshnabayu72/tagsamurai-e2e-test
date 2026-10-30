---
id: TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default
title: "Setup Column Registri: Pin Hideable dan Curated, Batas Pin Ketiga, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-233
  - TC-GS-TAG-234
  - TC-GS-TAG-235
  - TC-GS-TAG-236
coverage:
  web: automated
---

# Setup Column Registri: Pin Hideable dan Curated, Batas Pin Ketiga, dan Reset to Default

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata; keputusan D-3, pola File Manager).
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (respons yang dipaksa; endpoint dari `tc-all-tags-backend.md`, yang menyebut LLD dan OpenAPI modul; skema respons mengikuti openapi modul dan dilengkapi tahap script, S-13):
  - Daftar registri: `POST /v2/hardware-tagging/tags/list` (`tc-all-tags-backend.md` bagian 1). Mengembalikan 30 baris Seed Registri A (DD-01 sampai DD-30; 4 Paired dan 26 Not Paired; ukuran halaman 10) beserta kolom Last Scanned In, Activated At, dan Last User.
  - Kartu counter lisensi: `GET /v2/hardware-tagging/tags/license-counters` (bagian 2) dan kartu counter kesehatan: `GET /v2/hardware-tagging/tags/health-counters` (bagian 3), dipanggil halaman saat dibuka. Nilainya bebas dan tidak diasersi spec ini.
  - Opsi filter: `POST /v2/hardware-tagging/tags/options` (bagian 4), hanya bila halaman memuatnya saat dibuka. Tidak menjadi objek langkah spec ini.
  - Stream atau langganan real-time halaman TAG: tidak didefinisikan di sumber yang dibaca tahap ini; bila halaman berlangganan, stream di-mock tanpa event dan disediakan tim FE (S-13).
  - Respons preferensi Guided Tooltip untuk `guided_tooltip_seen_gs-tag-registry`: true (di-mock). API pendukung di luar modul (identitas pengguna, sesi, menu, preferensi Guided Tooltip, General Settings) disediakan tim FE (S-13).
- Preferensi kolom (visibilitas, urutan, pin) diperlakukan sebagai pengaturan sisi klien yang tidak melewati API TAG; mekanisme penyimpanannya tidak didefinisikan di TC (lihat Temuan untuk QA), sehingga tidak ada endpoint yang di-mock untuknya. "Tekan F5" dilakukan pada konteks browser yang sama supaya penyimpanan preferensi kolom dan intercept tetap ada.
- Lebar tabel registri harus melebihi lebar viewport (overflow horizontal), karena TC-GS-TAG-233 dan 234 hanya bermakna bila scroll horizontal teramati. Overflow dibuat oleh langkah 1 yang mempersempit viewport (lebar W ditetapkan tim FE; kemampuan teknis, Q-11) dan dipulihkan di langkah 28; data mock tidak dipakai untuk memaksa overflow.
- Data uji TC-GS-TAG-236 (precondition "konfigurasi sudah diubah dan tersimpan", nilainya tidak ditetapkan TC): hide `Brand`, seret `Status` ke posisi pertama, pin `Code`. Pilihan ini dibuat spec (lihat Temuan untuk QA).
- Suite serial (`parallel: false`): konfigurasi kolom registri adalah state global browser yang dipakai spec lain.
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`): pernyataan hook suite ada di `suite.md`; pada spec mock ini dipenuhi lewat respons preferensi Guided Tooltip yang di-mock true, sehingga walkthrough tidak muncul otomatis.
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom registri dikembalikan ke default dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; 10 kolom Hideable tampil, 3 kolom Curated tersembunyi, urutan awal, tanpa pin) dan viewport dikembalikan ke ukuran awal.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar, counter, dan opsi; mengatur viewport; scroll horizontal tabel; drag and drop elemen daftar kolom; mengarahkan kursor ke ikon Pin disabled untuk membaca tooltip.

## Test Steps

### TC-GS-TAG-233: Pin kolom Hideable membekukan kolom saat scroll horizontal

1. Persempit viewport sampai tabel registri overflow horizontal (lebar viewport W ditetapkan tim FE)
2. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
3. Klik ikon Pin kolom `Code`
4. Klik `Save`
5. Scroll tabel secara horizontal
6. Verifikasi kolom `Code` tetap di kiri saat tabel di-scroll horizontal
7. Tekan F5
8. Scroll tabel secara horizontal
9. Verifikasi kolom `Code` tetap di kiri saat tabel di-scroll horizontal setelah F5 (pin persist)
10. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
11. Klik ikon Pin kolom `Code` lagi untuk melepas
12. Klik `Save`
13. Scroll tabel secara horizontal
14. Verifikasi kolom `Code` ikut bergeser saat tabel di-scroll horizontal (pin terlepas)
15. Scroll tabel horizontal kembali ke posisi awal

### TC-GS-TAG-234: Pin kolom Curated

16. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
17. Centang `Last Scanned In`
18. Klik `Save`
19. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
20. Klik ikon Pin kolom `Last Scanned In`
21. Klik `Save`
22. Scroll tabel secara horizontal
23. Verifikasi kolom `Last Scanned In` membeku di kiri saat tabel di-scroll horizontal
24. Tekan F5
25. Scroll tabel secara horizontal
26. Verifikasi kolom `Last Scanned In` tetap membeku di kiri setelah F5 (pin persist)
27. Scroll tabel horizontal kembali ke posisi awal
28. Pulihkan viewport ke ukuran awal
29. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
30. Klik `Reset to Default`
31. Klik `Save`

### TC-GS-TAG-235: Pin ke-4 diblok

32. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
33. Pin `TAG Type`, `Code`, dan `Device Name`
34. Arahkan kursor ke ikon Pin kolom `SKU`
35. Verifikasi ikon Pin kolom `SKU` disabled
36. Verifikasi tooltip ikon Pin disabled `Maximum 3 columns can be pinned at once. Unpin another column first.`
37. Unpin `Device Name`
38. Verifikasi ikon Pin kolom lain (`SKU`) aktif kembali
39. Klik `[✕]` untuk menutup modal tanpa Save

### TC-GS-TAG-236: Reset to Default mengembalikan konfigurasi bawaan setelah Save

40. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
41. Hapus centang `Brand`
42. Seret `Status` ke posisi pertama
43. Pin `Code`
44. Klik `Save`
45. Buka modal Setup Column lewat header kolom Actions (⋯) dan item `Setup Column...`
46. Klik `Reset to Default`
47. Verifikasi preview menampilkan 10 kolom Hideable (`TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned`)
48. Verifikasi preview menyembunyikan 3 kolom Curated (`Last Scanned In`, `Activated At`, `Last User`)
49. Verifikasi preview tanpa kolom yang di-pin
50. Verifikasi preview berurutan sesuai urutan awal
51. Klik `Save`
52. Verifikasi tabel menampilkan 10 kolom Hideable (`TAG Type`, `Code`, `Device Name`, `SKU`, `Brand`, `Model/Type`, `Source`, `Type`, `Status`, `Last Scanned`)
53. Verifikasi tabel menyembunyikan 3 kolom Curated (`Last Scanned In`, `Activated At`, `Last User`)
54. Verifikasi tabel tanpa kolom yang di-pin
55. Verifikasi tabel berurutan sesuai urutan awal
56. Tekan F5
57. Verifikasi 10 kolom Hideable tetap tampil setelah F5
58. Verifikasi 3 kolom Curated tetap tersembunyi setelah F5
59. Verifikasi tabel tetap tanpa kolom yang di-pin setelah F5
60. Verifikasi tabel tetap berurutan sesuai urutan awal setelah F5

## Notes

- Mode: mock. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (233, 234, 235, 236). TC-GS-TAG-236 di akhir karena mengembalikan konfigurasi ke default sekaligus menjadi pemulihan state.
- Panjang spec: 60 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok satu kelas (Setup Column pin dan reset pada satu tabel registri, Mode mock, tanpa backend), tiap TC diakhiri pemulihan (langkah 15 dan 27, 28, 29 sampai 31, 39, 51 (`Save`)) sehingga berdiri sendiri; langkah 47 sampai 50 dan 52 sampai 60 adalah asersi TC-GS-TAG-236, bukan pemulihan, dan pemisahan hanya menambah hook tanpa memisahkan harness. Kegagalan keras pada pembukaan modal Setup Column akan memengaruhi semua blok; hal ini diakui.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 28 (mempersempit dan memulihkan viewport), langkah 15 dan 27 (mengembalikan posisi scroll), langkah 16 sampai 18 (precondition TC-GS-TAG-234 butir d: `Last Scanned In` dicentang dan tersimpan, dipakai sebagai precondition TC, tidak diasersi), langkah 29 sampai 31 (pemulihan ke default), langkah 39 (menutup modal tanpa Save sehingga pin sementara tidak tersimpan), langkah 40 sampai 44 (menyiapkan precondition TC-GS-TAG-236 butir d "konfigurasi sudah diubah dan tersimpan").
- "Klik Pin lagi melepas" dan "persist setelah F5" pada Expected TC-GS-TAG-233 serta "persist setelah F5" pada TC-GS-TAG-234 tidak punya langkah di TC; spec menulis langkah 7 sampai 14 dan 24 sampai 26 sebagai langkah menuju keadaan yang diasersi (S-14).
- Temuan untuk QA:
  - TC-GS-TAG-233 dan 234 tidak menyebut lebar viewport atau data yang membuat tabel overflow horizontal, padahal "scroll horizontal" hanya teramati bila konten melebihi lebar kontainer. Spec memakai kemampuan viewport (langkah 1 dan 28); lebar W ditetapkan tim FE atau dikonfirmasi lewat lebar minimum kolom (Q-11).
  - TC-GS-TAG-235 butir b menyebut "salah satu di-unpin" tanpa menyebut kolom; spec memilih `Device Name`.
  - TC-GS-TAG-236 precondition d ("konfigurasi sudah diubah dan tersimpan") tidak menyebut kolom dan nilai konkret; spec memilih sendiri (hide `Brand`, `Status` ke posisi pertama, pin `Code`) dan menyalin langkah penyiapan (S-04).
  - Mekanisme persistensi konfigurasi kolom (penyimpanan browser atau API) tidak didefinisikan di TC maupun `tc-all-tags-backend.md`; spec mock tidak mengarang endpoint, dan bila persistensi ternyata lewat API, endpoint tambahan disediakan tim FE (S-13).
  - TC-GS-TAG-236 butir a mengelompokkan "10 kolom Hideable tampil, 3 Curated Hidden, tanpa pin, urutan awal" dalam satu butir; spec memecahnya menjadi empat `Verifikasi` (langkah 47 sampai 50).
