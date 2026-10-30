---
id: TC-GS-DIV-E2E-030-konflik-edit-vs-delete-record-dihapus-pihak-lain
title: "Konflik Edit vs Delete dan Bulk Delete: Record Dihapus Pihak Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-113
  - TC-GS-DIV-275
  - TC-GS-DIV-276
coverage:
  web: automated
---

# Konflik Edit vs Delete dan Bulk Delete: Record Dihapus Pihak Lain

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama, pihak yang menyimpan Edit): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua, pihak yang menghapus): Total Control (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Tabel Pre-setup TC Division tidak mencantumkan akun ini; disediakan tim FE (cara yang sama dengan suite Brand).
- Sesi A berjalan di konteks browser dengan sesi login sendiri (seedSession di hook `before`, kredensial dari env var) dan berada di Global Settings > User > Division. Sesi B dipakai dalam dua bentuk: sesi API (klien HTTP dengan kredensial Admin B; cara memperoleh token disediakan tim FE) sebagai pemicu penghapusan pada TC-GS-DIV-113 dan TC-GS-DIV-275 karena tidak ada asersi di Sesi B, dan konteks browser kedua (login di hook `before`, berada di Global Settings > User > Division) pada TC-GS-DIV-276 karena toast dan baris tabel diasersi di Sesi B. Hook `after` menutup konteks browser Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding Division lewat API di hook `before`, semuanya bebas relasi; milik spec ini, pengganti `Training`, `Temp Unit`, `Rapid Unit`, dan `Spare Unit` pada TC sumber; tidak menumpang spec lain): `Training {runId}-030` dengan Code `E30A` (TC-GS-DIV-113), `Temp Unit {runId}-030` dengan Code `E30B` (TC-GS-DIV-275), `Rapid Unit {runId}-030` dengan Code `E30C` dan `Spare Unit {runId}-030` dengan Code `E30D` (TC-GS-DIV-276), serta `Anchor Unit {runId}-030` dengan Code `E30E` (baris pembanding yang tetap ada untuk asersi baris tidak ada pada ketiga TC; tidak dihapus oleh Sesi B). Division selain `Anchor Unit` dihapus oleh Sesi B pada spec ini. Nama yang dicoba disimpan Sesi A (`Training Center {runId}-030`, `Temp Unit 2 {runId}-030`, `Rapid Unit 2 {runId}-030`) tidak boleh pernah tersimpan.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API kelima nama seeding dan ketiga nama yang dicoba disimpan di atas, serta Division berkode `E30A` sampai `E30E`, bila masih ada. Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: konteks browser Sesi A dan Sesi B yang berjalan paralel; klien HTTP untuk sesi API Sesi B (`DELETE /v2/iam/divisions`); membaca request daftar Division (`POST /v2/iam/divisions/list`) untuk memastikan daftar di-refresh; langkah ditandai `[Sesi A]` dan `[Sesi B]`; Sesi A menahan modal Edit tetap terbuka saat Sesi B menghapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan

1. [Sesi A] Ketik Search `{runId}-030`, tekan Enter

### TC-GS-DIV-113: Edit Division yang sudah dihapus pihak lain menampilkan toast tidak tersedia

2. [Sesi A] Buka row action baris `Training {runId}-030` lalu klik `Edit`
3. [Sesi B] Hapus Division `Training {runId}-030` lewat sesi API
4. [Sesi A] Ubah Division Name menjadi `Training Center {runId}-030`
5. [Sesi A] Klik `[Save]`
6. [Sesi A] Verifikasi toast netral: `This division is no longer available.`
7. [Sesi A] Verifikasi modal Edit tertutup
8. [Sesi A] Verifikasi daftar Division di-refresh (request daftar Division dimuat ulang)
9. [Sesi A] Verifikasi baris `Anchor Unit {runId}-030` tampil di tabel (pembanding)
10. [Sesi A] Verifikasi baris `Training {runId}-030` tidak ada di tabel
11. [Sesi A] Verifikasi perubahan tidak tersimpan (tidak ada baris `Training Center {runId}-030`)

### TC-GS-DIV-275: Edit-vs-Delete: Admin A menyimpan Edit pada Division yang baru dihapus Admin B

12. [Sesi A] Buka row action baris `Temp Unit {runId}-030` lalu klik `Edit`
13. [Sesi B] Hapus Division `Temp Unit {runId}-030` lewat sesi API
14. [Sesi A] Ubah Division Name menjadi `Temp Unit 2 {runId}-030`
15. [Sesi A] Klik `[Save]`
16. [Sesi A] Verifikasi toast netral: `This division is no longer available.`
17. [Sesi A] Verifikasi modal Edit tertutup
18. [Sesi A] Verifikasi daftar Division di-refresh (request daftar Division dimuat ulang)
19. [Sesi A] Verifikasi baris `Anchor Unit {runId}-030` tampil di tabel (pembanding)
20. [Sesi A] Verifikasi baris `Temp Unit {runId}-030` tidak ada di tabel
21. [Sesi A] Verifikasi tidak ada Division `Temp Unit 2 {runId}-030` yang dibuat

### TC-GS-DIV-276: Edit-vs-Bulk Delete: Admin A menyimpan Edit pada Division yang baru dihapus lewat Bulk Delete Admin B

22. [Sesi A] Buka row action baris `Rapid Unit {runId}-030` lalu klik `Edit`
23. [Sesi B] Muat ulang halaman Division
24. [Sesi B] Ketik Search `Unit {runId}-030`, tekan Enter
25. [Sesi B] Centang baris `Rapid Unit {runId}-030`
26. [Sesi B] Centang baris `Spare Unit {runId}-030`
27. [Sesi B] Klik aksi `[Delete]` pada Bulk Action Bar
28. [Sesi B] Klik `[Delete]` pada dialog `Delete Division`
29. [Sesi B] Verifikasi toast sukses: `Success, division has been deleted.`
30. [Sesi B] Verifikasi baris `Anchor Unit {runId}-030` tampil di tabel (pembanding)
31. [Sesi B] Verifikasi baris `Rapid Unit {runId}-030` dan `Spare Unit {runId}-030` tidak ada di tabel (Bulk Delete sukses untuk kedua Division)
32. [Sesi A] Ubah Division Name menjadi `Rapid Unit 2 {runId}-030`
33. [Sesi A] Klik `[Save]`
34. [Sesi A] Verifikasi toast netral: `This division is no longer available.`
35. [Sesi A] Verifikasi modal Edit tertutup
36. [Sesi A] Verifikasi daftar Division di-refresh (request daftar Division dimuat ulang)
37. [Sesi A] Verifikasi baris `Anchor Unit {runId}-030` tampil di tabel (pembanding)
38. [Sesi A] Verifikasi baris `Rapid Unit {runId}-030` tidak ada di tabel
39. [Sesi A] Verifikasi tidak ada Division `Rapid Unit 2 {runId}-030`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-113, 275, 276). Mode: FE+BE. Kelas harness: multi-konteks (dua admin, bagian 3 prinsip 13c).
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC mengikuti urutan nomor TC sumber (113, 275, 276); Delete oleh Sesi B menghapus Division milik tiap TC sehingga tiap blok memakai Division sendiri dan tidak saling bergantung.
- Pembagian TC lintas spec: Delete single dan Bulk Delete oleh Sesi B hanya berfungsi sebagai pemicu state (pihak lain menghapus record) dan bukan objek asersi; objek asersi adalah hasil Save Sesi A. Sesi B memakai sesi API pada TC-GS-DIV-113 dan TC-GS-DIV-275 karena tidak ada asersi di Sesi B, dan sesi UI pada TC-GS-DIV-276 karena Expected a (Bulk Delete sukses) diasersi di Sesi B. Perilaku Delete single pada record yang sudah dihapus pihak lain (idempotent, toast `Success, division has been deleted.`, NC-03 dan NC-08) ada di spec `TC-GS-DIV-E2E-033-konflik-delete-in-use-saat-confirm-dan-sudah-dihapus`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pencarian `{runId}-030` supaya seluruh Division milik spec tampil; Search Sesi A tidak diganti selama spec), langkah 23 (muat ulang agar tabel Sesi B menampilkan data terbaru), dan langkah 24 (pencarian `Unit {runId}-030` di Sesi B supaya `Rapid Unit` dan `Spare Unit` tampil bersamaan).
- Asersi tambahan: langkah 7, 17, dan 35 (modal Edit tertutup setelah toast netral) tidak ada di Expected TC; ditambahkan karena TC tidak menyebut keadaan modal sesudah toast dan asersi tabel sesudahnya mengandalkan modal yang sudah tertutup. Langkah 9, 19, 30, dan 37 (baris `Anchor Unit` tampil) adalah baris pembanding sebelum asersi baris tidak ada (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-DIV-113, 275, dan 276 tidak menyebut keadaan modal Edit Sesi A sesudah toast `This division is no longer available.`; spec mengasersi modal tertutup dan perlu dikonfirmasi QA.
  - TC-GS-DIV-113 dan TC-GS-DIV-275 hampir identik (Division berbeda, Expected sama); keduanya dipertahankan sebagai blok terpisah sesuai sourceTc.
  - TC-GS-DIV-113 precondition c (Population D-02 termasuk `Accounting`) tidak dipakai langkahnya; spec memakai Division milik spec.
  - TC-GS-DIV-276 tidak menyebut kondisi seleksi tabel Sesi B (Search yang dipakai); spec mencari `Unit {runId}-030` agar kedua Division terlihat bersamaan.
- Spec melewati sekitar 35 langkah (39 langkah) karena memuat tiga TC konflik Edit vs Delete yang masing-masing butuh aksi dua sesi; seluruhnya satu kelas harness (multi-konteks), memakai satu Search dan satu dataset bersuffix, dan tiap blok memakai Division sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
