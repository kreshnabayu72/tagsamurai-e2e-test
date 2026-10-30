---
id: TC-GS-DIV-E2E-071-import-create-missing-divisions-edit-delete-dan-log
title: "Import Create Missing Divisions: Edit, Delete In-Use, dan Pencatatan Create"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-256
  - TC-GS-DIV-257
  - TC-GS-DIV-258
coverage:
  web: automated
---

# Import Create Missing Divisions: Edit, Delete In-Use, dan Pencatatan Create

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh data milik spec ini):
  - Draft Staging Table Import Type `User Login` yang memuat satu baris berstatus `error` dengan Division `Import Division A {runId}-071` yang belum ada (D-16). Draft disiapkan di hook `before` dan setara langkah "jalankan Import User Login hingga Staging Table menampilkan Division yang belum ada" pada dependensi TC-GS-DIV-256. Hook `before` lebih dulu membuang draft aktif Import Type `User Login` bila ada (Single Active Draft).
  - Division `Import Division A {runId}-071` (D-16): dibuat lewat tombol `[Create Missing Divisions]` pada langkah 2 (Code di-generate otomatis), lalu di-rename menjadi `Import Division B {runId}-071` pada TC-GS-DIV-256.
  - Login User uji `importuser+{runId}-071@qwertysystem.net` dengan Division `Import Division B {runId}-071`: di-seed lewat API pada langkah 17 supaya Division itu in-use pada TC-GS-DIV-257 (setara "dipakai oleh user hasil Import"). Nilai field wajib lain disediakan tim FE lewat fixture `fixtures/division.json` yang belum ada.
- Kemampuan teknis (disediakan tim FE; mekanismenya tidak didefinisikan TC, PRD, atau LLD): menyiapkan dan membuang draft Staging Table Import `User Login` lewat API dengan satu baris ber-Division yang belum ada; seeding Login User lewat API; penghapusan Division dan Login User lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): buang draft aktif Import `User Login`, hapus lewat API Login User `importuser+{runId}-071@qwertysystem.net`, lalu Division `Import Division A` atau `Import Division B` bersuffix `{runId}-071` yang masih ada. Entri log bersifat immutable dan tidak dihapus.
- State global yang diubah: draft aktif Import Type `User Login` (dibuang di hook `before` dan `after`). Suite berjalan serial (`suite.md`, `parallel: false`).
- TC-GS-DIV-256, 257, 258: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### Dependensi TC-GS-DIV-256: Create Missing Divisions dari Import User Login

1. Buka Global Settings > Import, pilih Import Type `User Login`
2. Klik `⋯` pada baris ber-Division `Import Division A {runId}-071` > `[Create Missing Divisions]`
3. Verifikasi toast sukses: "Success, division has been created."

### TC-GS-DIV-258: Division hasil Create Missing Divisions tercatat sebagai Create biasa

4. Buka Global Settings > User > Division, buka Modal Changelog, ketik Search `Import Division A {runId}-071`, tekan Enter
5. Verifikasi Changelog: tepat 1 entri dengan Action `Create` (tanpa qualifier khusus), Division Name `Import Division A {runId}-071`, Field `Division Name`, Old Value `—`, New Value `Import Division A {runId}-071`
6. Verifikasi Changelog: Modified By entri itu `Sari D` (aktor yang mengklik tombol `[Create Missing Divisions]`)
7. Tutup Modal Changelog, buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `Import Division A {runId}-071`, tekan Enter
8. Verifikasi System Log Sari Dewi: tepat 1 entri dengan Action `Create`, Object `Division`, Name `Import Division A {runId}-071`, Field `Division Name`, Old Value `—`, New Value `Import Division A {runId}-071`
9. Buka Global Settings > Activity Log, ketik Search `Import Division A {runId}-071`, tekan Enter
10. Verifikasi Activity Log: tepat 1 entri dengan Action `Create`, Object `Division`, Name `Import Division A {runId}-071`

### TC-GS-DIV-256: Division hasil Create Missing Divisions dapat di-Edit identik dengan Create manual

11. Buka Global Settings > User > Division, ketik Search `Import Division A {runId}-071`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Import Division B {runId}-071`, klik [Save]
12. Verifikasi toast sukses: "Success, division has been updated."
13. Verifikasi baris tabel menampilkan Division Name `Import Division B {runId}-071`
14. Verifikasi kolom Code baris `Import Division B {runId}-071` terisi (Code hasil auto-generate tetap tampil)
15. Buka Modal Changelog, ketik Search `Import Division B {runId}-071`, tekan Enter
16. Verifikasi Changelog: entri Edit dengan Division Name `Import Division B {runId}-071`, Field `Division Name`, Old Value `Import Division A {runId}-071`, New Value `Import Division B {runId}-071`

### TC-GS-DIV-257: Division hasil Create Missing Divisions mengikuti guard in-use dan Delete yang sama

17. Seed Login User uji `importuser+{runId}-071@qwertysystem.net` dengan Division `Import Division B {runId}-071` lewat API
18. Tutup Modal Changelog, ganti isi kotak search dengan `Import Division B {runId}-071`, tekan Enter pada tabel Division, klik `⋯` pada baris tersebut > Delete
19. Verifikasi dialog `Cannot Delete Data` tampil
20. Verifikasi dialog memuat `Import Division B {runId}-071`
21. Verifikasi dialog memuat tombol `[OK]`
22. Klik [OK]

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Spec ini lintas modul (Import); objek ujinya Division hasil `[Create Missing Divisions]` (`global-settings/import/PRD/import.md`, `IMP-LOGIC-11`).
- Urutan TC di spec berbeda dari urutan sumber: 258 (pencatatan Create) dibaca lebih dulu daripada 256 (Edit), karena TC-GS-DIV-258 membaca entri Create yang dihasilkan langkah 2 dan entri Edit pada TC-GS-DIV-256 tidak boleh mendahuluinya; 257 paling akhir karena memerlukan Division yang sudah di-rename dan tidak menghapus data (dialog diblokir).
- Dependensi TC-GS-DIV-256 (membuat `Import Division A` lewat `[Create Missing Divisions]`) dijalankan sebagai langkah 1 sampai 3 di spec ini; draft Staging Table disiapkan di hook `before`. Toast sukses pada langkah 3 adalah asersi tambahan (teks dari PRD Import) yang menandai Division sudah dibuat sebelum langkah berikutnya; bukan Expected Result TC.
- Langkah 1 membuka Global Settings > Import (layar modul Import, bukan layar awal Division) karena Staging Table Import adalah sumber aksi `[Create Missing Divisions]`.
- Entri log dikenali lewat nama bersuffix `{runId}-071`; entri milik run lain diabaikan.
- Aksi per baris (`⋯` > `[Create Missing Divisions]`, langkah 2) dipilih supaya hanya baris itu yang diproses; TC sumber hanya menulis "tombol `[Create Missing Divisions]`" tanpa menyebut per-baris atau bulk dari Error Summary Callout.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 7, 9, 11, dan 15 (membuka surface log dan tab Division, lalu Search nama entri), Search nama Division pada tabel Division sebelum Edit dan Delete (langkah 11 dan 18; tabel A-Z memiliki lebih dari satu halaman), langkah 17 (seeding Login User supaya Division in-use), dan penutupan Modal Changelog pada langkah 18.
- Expected Result TC-GS-DIV-257 ("Dialog `Cannot Delete Data` tampil ... `Import Division B` dan `[OK]`") dipecah menjadi langkah 19, 20, dan 21; judul dialog `Cannot Delete Data` dan tombol `[OK]` mengikuti PRD Division §4.2d Dialog 2.
- Spec dengan aksi serupa untuk Division buatan manual ada di spec Edit dan Delete; spec `TC-GS-DIV-E2E-072-import-create-missing-divisions-limit-dan-race` memuat penolakan Create Missing karena Master Data Count Limit dan race duplicate.
- Temuan untuk QA:
  - TC-GS-DIV-256 Expected Result b ("Name dan Code ter-update") ambigu: Edit hanya mengubah Name, sehingga Code tidak berubah; spec memverifikasi Name baru tampil dan Code tetap terisi (langkah 13 dan 14).
  - TC-GS-DIV-256 Expected Result c ("Entri Edit tercatat di Changelog") tidak menyebut kolom entri; spec memverifikasi Action, Division Name, Field, Old Value, dan New Value mengikuti pola PRD Division §8.1.
  - TC-GS-DIV-257 Precondition c ("dipakai oleh user hasil Import") tidak menyebut cara user terbentuk; spec men-seed Login User lewat API pada langkah 17 (bukan commit Import) dan cara itu perlu disediakan tim FE.
  - TC-GS-DIV-256 dan 258 tidak menyebut cara mempersiapkan Staging Table Import User Login (berkas, Column Mapping) dan lokasi tombol `[Create Missing Divisions]`; kebutuhan itu ditulis di Prerequisites sebagai kemampuan teknis tim FE.
