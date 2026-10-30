---
id: TC-GS-DIV-E2E-074-state-tenant-write-lockdown-suspended-dan-expired
title: "State Tenant: Create, Edit, dan Delete Ditolak saat Entitas Suspended atau Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-263
  - TC-GS-DIV-264
  - TC-GS-DIV-265
coverage:
  web: automated
---

# State Tenant: Create, Edit, dan Delete Ditolak saat Entitas Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pengubah status Client A (hanya lewat API, tanpa login UI) | Total Control Principal | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Akun Principal tidak tercantum di Tabel Data Uji Pre-setup Division; akun dan hak ubah status Client A disediakan tim FE. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah; target Edit dan Delete adalah Division milik spec.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API (kemampuan seeding Division lewat API) di hook `before` saat Client A Active, Code di-generate otomatis:
  - `Treasury {runId}-074` (bebas relasi): target Delete pada TC-GS-DIV-265 (setara `Treasury` pada TC).
  - `Finance {runId}-074` (bebas relasi): target Edit pada TC-GS-DIV-264 (setara `Finance` pada TC).
  - Input uji `Suspended Create` (TC-GS-DIV-263) dan `Finance Expired {runId}-074` (Name baru TC-GS-DIV-264) adalah input yang ditolak sehingga tidak membuat data.
- Kemampuan teknis: (a) mengubah status Client A menjadi Suspended dan Expired lalu memulihkannya ke Active lewat API dengan sesi akun Principal di atas, sebagai langkah eksplisit di spec; (b) membaca status respons request tulis Create, Edit, dan Delete Division (`403`); (c) memuat ulang halaman dengan dialog bawaan browser `beforeunload` dikonfirmasi otomatis oleh harness, untuk menutup form atau dialog yang masih terbuka tanpa langkah bersyarat.
- Syarat eksekusi: status Client A diubah untuk seluruh tenant, sehingga spec ini dijalankan sendiri pada tahap atau suite terpisah tanpa spec Client A lain yang berjalan bersamaan (suite Division berjalan serial, `parallel: false`).
- State global yang dipulihkan: status Client A (diubah ke Suspended di langkah 1, Expired di langkah 23, dikembalikan ke Active di langkah 36; hook `after` tetap jalan walau spec gagal di tengah dan memulihkan status Client A ke Active lewat API dengan akun Principal).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan status Client A ke Active lebih dulu, lalu hapus lewat API `Treasury {runId}-074`, `Finance {runId}-074`, `Finance Expired {runId}-074`, dan `Suspended Create` bila ada.
- TC-GS-DIV-263 dan 265: Client A berstatus Suspended. TC-GS-DIV-264: Client A berstatus Expired. Ketiganya: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-263: Create saat entitas Suspended ditolak server

1. Ubah status Client A menjadi Suspended (lewat API dengan akun Principal)
2. Muat ulang halaman Global Settings > User > Division
3. Klik `[+ Division]`
4. Isi Division Name `Suspended Create`
5. Klik [Submit]
6. Verifikasi server menolak dengan `403 Forbidden`
7. Verifikasi toast error: `Changes can't be saved while this workspace is suspended or expired.`
8. Muat ulang halaman Global Settings > User > Division
9. Ketik Search `Treasury {runId}-074`, tekan Enter pada tabel Division
10. Verifikasi Division `Treasury {runId}-074` tampil di tabel
11. Ganti isi kotak search dengan `Suspended Create`, tekan Enter
12. Verifikasi Division `Suspended Create` tidak dibuat (tidak ada di tabel)
13. Klik `(←)` pada kotak Search

### TC-GS-DIV-265: Delete saat entitas Suspended ditolak server

14. Ketik Search `Treasury {runId}-074`, tekan Enter pada tabel Division
15. Klik `⋯` pada baris `Treasury {runId}-074` > Delete
16. Klik [Delete] pada dialog `Delete Division`
17. Verifikasi server menolak dengan `403 Forbidden`
18. Verifikasi toast error: `Changes can't be saved while this workspace is suspended or expired.`
19. Muat ulang halaman Global Settings > User > Division
20. Ketik Search `Treasury {runId}-074`, tekan Enter pada tabel Division
21. Verifikasi Division `Treasury {runId}-074` tetap ada di tabel
22. Klik `(←)` pada kotak Search

### TC-GS-DIV-264: Edit saat entitas Expired ditolak server

23. Ubah status Client A menjadi Expired (lewat API dengan akun Principal)
24. Muat ulang halaman Global Settings > User > Division
25. Ketik Search `Finance {runId}-074`, tekan Enter pada tabel Division
26. Klik `⋯` pada baris `Finance {runId}-074` > Edit
27. Ubah Division Name menjadi `Finance Expired {runId}-074`
28. Klik [Save]
29. Verifikasi server menolak dengan `403 Forbidden`
30. Verifikasi toast error: `Changes can't be saved while this workspace is suspended or expired.`
31. Muat ulang halaman Global Settings > User > Division
32. Ketik Search `{runId}-074`, tekan Enter pada tabel Division
33. Verifikasi Name `Finance {runId}-074` tidak berubah (baris `Finance {runId}-074` tetap ada)
34. Verifikasi Division `Finance Expired {runId}-074` tidak ada di tabel
35. Klik `(←)` pada kotak Search
36. Pulihkan status Client A ke Active (lewat API dengan akun Principal)

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas state tenant (prinsip 13h): write-lockdown Suspended dan Expired; tidak ada TC verifikasi baca murni di spec ini.
- Spec melewati sekitar 35 langkah (36) karena tiga TC masing-masing memuat muat ulang, pencarian anchor, aksi yang ditolak, dan asersi absence; satu kelas (13h), tiap blok TC memakai Division seed sendiri, dan ketiganya berbagi dua perubahan status Client A (Suspended lalu Expired) yang mahal bila diulang.
- Urutan TC di spec berbeda dari urutan sumber (263, 265, 264): dua TC bersyarat Suspended (263 dan 265) berurutan, lalu status diubah ke Expired untuk 264, sehingga status Client A hanya berubah dua kali. Semua aksi ditolak sehingga tidak ada data berubah atau terhapus.
- Target Edit dan Delete adalah Division seed milik spec (`Finance {runId}-074`, `Treasury {runId}-074`; S-06); Division Pre-setup `Finance` dan `Treasury` tidak disentuh spec ini.
- Penolakan mengikuti keputusan NC-04 (`403 Forbidden`); asersi `403` diambil dari respons request tulis yang dipicu UI.
- Asersi absence (langkah 12 dan 34) didahului anchor positif pada tabel yang sama (langkah 10 dan 33; bagian 8b butir 2).
- Langkah penghubung: langkah 1, 23, dan 36 (mengubah atau memulihkan status Client A; precondition TC menyebut entitas Suspended atau Expired dijadikan langkah eksplisit); langkah 2, 24 (memuat ulang halaman sesudah status berubah); langkah 8, 19, dan 31 (memuat ulang halaman sesudah penolakan supaya form atau dialog yang masih terbuka tertutup dan tabel dibaca ulang; TC tidak menyebut keadaan form sesudah penolakan); langkah 9, 11, 14, 20, 25, dan 32 (Search nama yang diasersi atau menjadi target baris); langkah 13, 22, dan 35 (mengosongkan Search).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-DIV-263, 264, 265: TC dan PRD tidak menyebut apakah modal Create/Edit atau dialog Delete menutup setelah penolakan; spec memuat ulang halaman (dengan `beforeunload` dikonfirmasi) agar tidak ada langkah bersyarat. Spec juga mengasumsikan aksi baca (Search, daftar Division) tetap berfungsi saat Suspended atau Expired (PRD D1 hanya menyebut aksi tulis ditolak).
  - TC-GS-DIV-264: TC tidak memberi Name baru untuk Edit `Finance`; spec memakai `Finance Expired {runId}-074`.
  - TC-GS-DIV-263, 264, 265: cara mengubah status Client A dan akun pengubahnya tidak didefinisikan TC; disediakan tim FE (Principal mengikuti suite Brand).
