---
id: TC-GS-DIV-E2E-072-import-create-missing-divisions-limit-dan-race
title: "Import Create Missing Divisions: Master Data Count Limit dan Duplicate Race"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-289
  - TC-GS-DIV-290
coverage:
  web: automated
---

# Import Create Missing Divisions: Master Data Count Limit dan Duplicate Race

## Prerequisites

- Mode: FE+BE. Spec race dan limit Import lintas modul (Import): Master Data Count Limit Division diubah sebagai pemicu state (P-2) dan Admin B hanya memicu pembuatan Division lewat API.
- Akun yang diuji (spec memakai satu sesi UI dan satu sesi API terpisah):

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Admin A (sesi UI) | Total Control, Sari Dewi (`Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Admin B (hanya lewat API, tanpa login UI) | Total Control (admin kedua), Nadia Pratama (`Nadia P`) | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `GS_TC2_PASSWORD` |

  Akun Admin B tidak tercantum di Tabel Data Uji Pre-setup; akun ini disediakan tim FE. Login Admin A di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (`GS_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh data milik spec ini):
  - Draft Staging Table Import Type `User Login` yang memuat dua baris berstatus `error` dengan Division yang belum ada: `Limit Import Unit {runId}-072` dan `Race Import Unit {runId}-072`. Draft disiapkan di hook `before` (setara langkah "jalankan Import User Login hingga Staging Table menampilkan Division yang belum ada"); hook `before` lebih dulu membuang draft aktif Import Type `User Login` bila ada (Single Active Draft).
  - Division `Race Import Unit {runId}-072` dengan Code `RIU`: dibuat Admin B lewat API pada langkah 16 (setara pembuatan lewat `[+ Division]` oleh admin lain pada Precondition c TC-GS-DIV-290). Code `RIU` literal sesuai TC (pengecualian S-12: seeding idempotent, cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial); hook `before` menghapus lewat API sisa Division bernama `Race Import Unit {runId lama}-072` (nama berpola `Race Import Unit *-072`, bukan berdasarkan Code saja) yang masih memegang Code `RIU`.
  - `Limit Import Unit {runId}-072` tidak boleh terbentuk; tidak ada data yang dibuat untuknya.
- State global yang diubah: Master Data Count Limit Division entitas Total Control Client A (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits). Hook `before` mencatat nilai awalnya, menghitung jumlah Division Client A `{N}` sesudah seeding selesai (jumlah Division saat ini: Division Pre-setup, Population, dan Division milik spec lain yang masih ada), dan mengatur limit sama dengan `{N}` (Precondition b TC-GS-DIV-289), sehingga tidak ada slot tersisa. Langkah 14 mengembalikan limit ke nilai awal sebelum TC-GS-DIV-290; hook `after` mengembalikannya lagi sebagai cadangan. Suite berjalan serial (`parallel: false`) karena limit ini dipakai bersama seluruh spec suite.
- Kemampuan teknis (disediakan tim FE; mekanismenya tidak didefinisikan TC, PRD, atau LLD): mengubah dan memulihkan Master Data Count Limit lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, dengan akun dan hak ubah yang disediakan tim FE (TC, PRD, dan LLD tidak menyebut akun pelakunya); menyiapkan dan membuang draft Staging Table Import `User Login` lewat API; Admin B sebagai sesi API terpisah (login lewat API dengan `Spectra.env.GS_TC2_PASSWORD`) yang membuat Division di antara pembacaan Staging Table dan klik tombol; penghapusan Division lewat API.
- Cleanup (hook `after`, tidak berasumsi langkah berhasil penuh): pulihkan Master Data Count Limit ke nilai awal, buang draft aktif Import `User Login`, dan hapus lewat API Division `Race Import Unit {runId}-072` dan `Limit Import Unit {runId}-072` bila ada. Entri log bersifat immutable dan tidak dihapus.
- Baseline log: sesudah hook `before` selesai dan sebelum aksi pertama, spec mencatat jumlah total entri Changelog `{nChangelog}` pada langkah 1.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- TC-GS-DIV-289 dan 290: login sebagai Total Control (Admin A).

## Test Steps

### TC-GS-DIV-289: Create Missing Divisions saat Master Data Count Limit tercapai ditolak

1. Buka Modal Changelog, catat jumlah total entri Changelog sebagai baseline `{nChangelog}`
2. Tutup Modal Changelog, buka Global Settings > Import, pilih Import Type `User Login`
3. Klik `⋯` pada baris ber-Division `Limit Import Unit {runId}-072` > `[Create Missing Divisions]`
4. Verifikasi toast error: "Error, failed to create division."
5. Verifikasi baris Tab User dengan Division `Limit Import Unit {runId}-072` tetap berstatus `error` di Staging Table
6. Buka Global Settings > User > Division
7. Verifikasi jumlah Division pada tabel tetap `{N}`, sama dengan Master Data Count Limit
8. Ketik Search `Limit Import Unit {runId}-072`, tekan Enter pada tabel Division
9. Verifikasi Division `Limit Import Unit {runId}-072` tidak dibuat: empty state `No results found`
10. Klik `(←)` pada kotak Search tabel Division
11. Buka Modal Changelog
12. Verifikasi jumlah total entri Changelog sama dengan baseline `{nChangelog}` (langkah 1)
13. Verifikasi Changelog tidak memuat entri `Create` baru untuk `Limit Import Unit {runId}-072` sejak baseline `{nChangelog}`

### TC-GS-DIV-290: Create Missing Divisions untuk nama yang sudah dibuat pihak lain ditolak sebagai duplicate

14. Tutup Modal Changelog, kembalikan Master Data Count Limit Division ke nilai awal (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits)
15. Buka Global Settings > Import, pilih Import Type `User Login` sehingga Staging Table dibaca dengan baris Division `Race Import Unit {runId}-072` yang belum ada
16. Admin B (sesi API atas akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`) membuat Division `Race Import Unit {runId}-072` dengan Code `RIU`
17. Klik `⋯` pada baris ber-Division `Race Import Unit {runId}-072` > `[Create Missing Divisions]`
18. Tunggu aksi selesai (indikator proses hilang dan menu aksi baris tersedia kembali)
19. Buka Global Settings > User > Division, ketik Search `Race Import Unit {runId}-072`, tekan Enter pada tabel Division
20. Verifikasi tabel Division memuat tepat 1 baris `Race Import Unit {runId}-072` (tidak ada Division ganda)
21. Verifikasi Code baris `Race Import Unit {runId}-072` tetap `RIU` (Division milik Admin B tidak dipakai ulang atau diubah)
22. Buka Global Settings > Import, pilih Import Type `User Login`
23. Verifikasi baris Tab User dengan Division `Race Import Unit {runId}-072` pulih ke status `pending` di Staging Table
24. Buka Global Settings > User > Division, buka Modal Changelog, ketik Search `Race Import Unit {runId}-072`, tekan Enter pada Modal Changelog
25. Verifikasi Changelog memuat tepat 1 entri `Create` untuk `Race Import Unit {runId}-072`
26. Verifikasi Modified By entri Create itu `Nadia P` (Division milik admin lain)

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Satu spec race dan limit Import: limit sebagai pemicu state (P-2) pada TC-GS-DIV-289 dan duplicate race dengan Admin B sebagai pemicu via API pada TC-GS-DIV-290, lintas modul Import (`global-settings/import/PRD/import.md`, `IMP-LOGIC-11`).
- Butir P-2: Admin B pada TC-GS-DIV-290 adalah sesi API yang hanya berfungsi sebagai pemicu Division yang sudah ada (bukan konteks kedua yang diasersi); sesi B tidak diasersi dan langkah 26 membaca entri Changelog di sesi UI Admin A. Pengaturan Master Data Count Limit pada TC-GS-DIV-289 dilakukan lewat kemampuan teknis di Prerequisites, bukan objek asersi.
- Butir P-1 dan S-05: TC-GS-DIV-289 Expected Result c bagian "tidak ada entri Create baru di Changelog" ditulis di spec ini (langkah 13) dengan baseline jumlah total entri langkah 1 dan pembanding jumlah langkah 12, karena spec absence `TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use` tidak memuat TC-GS-DIV-289. State berat (Master Data Count Limit sama dengan jumlah Division dan draft Staging Table) dibangun di spec ini dan dipakai bersama Expected Result a dan b.
- Urutan TC di spec: 289 lebih dulu karena memerlukan limit sama dengan jumlah Division; sesudahnya limit dikembalikan (langkah 14) supaya 290 hanya menguji duplicate, bukan limit. Kedua TC tidak menghapus data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencatat baseline jumlah total entri), 2, 6, 11, 15, 19, 22, dan 24 (membuka surface), langkah 8 (Search nama Division pada tabel), langkah 10 (mengosongkan Search sesudah asersi absence), langkah 14 (mengembalikan limit), langkah 15 (membaca ulang Staging Table sebelum Admin B bertindak), dan langkah 18 (menunggu klik `[Create Missing Divisions]` pada TC-GS-DIV-290 selesai karena hasil klik tidak diasersi langsung; modal atau indikator proses sudah hilang sebelum langkah 19). Tombol `[Create Missing Divisions]` dipilih lewat Actions (⋯) per baris (langkah 3 dan 17) karena draft memuat dua baris; TC sumber hanya menulis "tombol `[Create Missing Divisions]`".
- Asersi absence langkah 9 didahului anchor positif langkah 7 (tabel Division termuat dengan `{N}` baris tanpa Search; bagian 8b butir 2).
- Toast error pada langkah 4 adalah anchor positif (penolakan terhubung dengan pemicu) bagi asersi absence langkah 13 dan teksnya dari PRD Import (toast error `[Create Missing Divisions]`); bukan Expected Result TC.
- Langkah 21 adalah penjabaran "Division milik admin lain tidak dipakai ulang" (TC-GS-DIV-290 Expected Result a); langkah 26 adalah penjabaran "(milik admin lain)" pada Expected Result c TC-GS-DIV-290; langkah 23 mengikuti TC-GS-DIV-290 Expected Result b.
- Temuan untuk QA:
  - PRD Division `division.md` §9.6 (baris Create via Create Missing Divisions) menulis baris Tab User terkait "tetap `error`", sedangkan PRD Import `IMP-LOGIC-11` butir (3) dan TC-GS-DIV-290 Expected Result b menyatakan baris pulih ke `pending`; spec mengikuti TC dan PRD Import (langkah 23), selisih untuk pemilik PRD Division.
  - TC-GS-DIV-289 dan 290 tidak menyebut toast hasil klik tombol; PRD Import menyebut toast error `Error, failed to create division.` bila seluruh record gagal (langkah 4). TC-GS-DIV-290 tidak diasersi toast karena bukan Expected Result TC, meskipun PRD Import `:1168` menyebut toast error untuk nama yang sudah ada.
  - TC-GS-DIV-289 Precondition b dan c tidak menyebut akun, nilai awal limit, maupun cara menyiapkan Staging Table; Prerequisites mencantumkannya sebagai kemampuan tim FE. Mengubah Master Data Count Limit entitas Client A memengaruhi seluruh suite sehingga suite harus serial.
  - TC-GS-DIV-289 Expected Result c ("Jumlah Division tidak melebihi limit") tidak menyebut cara membaca jumlah Division; spec membandingkan jumlah baris tabel dengan `{N}` yang dihitung hook `before`.
