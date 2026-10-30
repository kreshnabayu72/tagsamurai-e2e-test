---
id: TC-GS-DIV-E2E-040-bulk-delete-race-item-menjadi-in-use
title: "Bulk Delete Race: Item Menjadi In-Use Setelah Pre-Check dan Saat Confirm"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-139
  - TC-GS-DIV-296
coverage:
  web: automated
---

# Bulk Delete Race: Item Menjadi In-Use Setelah Pre-Check dan Saat Confirm

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin). Spec menghapus data (TC-139) sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Akun Sesi A (Admin A): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B): Total Control admin kedua (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`, pada entitas yang sama dengan Sesi A. Akun tidak tercantum di Tabel Data Uji Pre-setup Division; disediakan tim FE (akun yang sama dengan Admin B suite Brand).
- Sesi A berjalan di konteks browser dengan sesi login sendiri (seedSession di hook `before`, kredensial dari env var) dan berada di Global Settings > User > Division. Sesi B memakai sesi API (klien HTTP dengan kredensial Admin B; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (kemampuan seeding Division dan seeding User lewat API di hook `before`; tidak menumpang spec lain), semua Division bebas relasi saat awal: `Audit Unit A {runId}-040` dan `Audit Unit B {runId}-040` (TC-296), serta `Research and Development {runId}-040` (setara RND) dan `Internal Control {runId}-040` (setara IC) (TC-139; dependensi TC-GS-DIV-30 dipenuhi lewat seeding). Tiga user uji milik spec (Login User, nama dan email bersuffix `{runId}-040`; nilai field wajib lain disediakan tim FE): user uji 1 dan user uji 2 untuk TC-296, user uji 3 untuk TC-139. Ketiganya memakai Division awal `Asal Uji {runId}-040`, sebuah Division milik spec yang dipakai user uji dan tidak diasersi. Code hasil seeding mengikuti auto-generate dan tidak diasersi.
- Kemampuan teknis: konteks browser Sesi A; klien HTTP untuk sesi API Sesi B; penugasan atau pemindahan Division user oleh Sesi B (pemicu race; endpoint penugasan tidak disebut TC, PRD, atau LLD Division, disediakan tim FE karena TC tidak menyebut caranya); langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API tiga user uji, lalu `Audit Unit A`, `Audit Unit B`, `Research and Development`, `Internal Control`, dan `Asal Uji` bersuffix `{runId}-040` bila masih ada, serta bersihkan Search dan seleksi tabel. Hook `beforeEach`: tutup dialog yang terbuka di Sesi A lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada (seluruh data milik spec dan dibersihkan).

## Test Steps

### Persiapan

1. [Sesi A] Ketik Search `{runId}-040`, tekan Enter

### TC-GS-DIV-296: Seluruh item menjadi in-use di antara buka dialog dan Confirm

2. [Sesi A] Centang baris `Audit Unit A {runId}-040`
3. [Sesi A] Centang baris `Audit Unit B {runId}-040`
4. [Sesi A] Klik `Bulk Action` > `Delete`
5. [Sesi B] Pindahkan user uji 1 ke Division `Audit Unit A {runId}-040` lewat sesi API
6. [Sesi B] Pindahkan user uji 2 ke Division `Audit Unit B {runId}-040` lewat sesi API
7. [Sesi A] Klik `[Delete]` pada dialog `Delete Division`
8. [Sesi A] Verifikasi tidak ada toast sukses
9. [Sesi A] Verifikasi tidak ada toast item dilewati
10. [Sesi A] Verifikasi dialog blokir in-use `Cannot Delete Data` tampil
11. [Sesi A] Verifikasi dialog memuat bullet `Audit Unit A {runId}-040` dan `Audit Unit B {runId}-040`
12. [Sesi A] Verifikasi dialog hanya punya tombol tunggal `[OK]`
13. [Sesi A] Klik `[OK]`
14. [Sesi A] Verifikasi baris `Audit Unit A {runId}-040` dan `Audit Unit B {runId}-040` tetap ada di tabel
15. [Sesi A] Verifikasi kedua baris tetap tercentang
16. [Sesi A] Verifikasi counter `2 Divisions selected`
17. [Sesi A] Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-139: Item berubah in-use setelah pre-check di-skip diam-diam ke ringkasan

18. [Sesi A] Centang baris `Research and Development {runId}-040`
19. [Sesi A] Centang baris `Internal Control {runId}-040`
20. [Sesi A] Klik `Bulk Action` > `Delete`
21. [Sesi B] Tugaskan Division `Internal Control {runId}-040` ke user uji 3 lewat sesi API
22. [Sesi A] Klik `[Delete]` pada dialog `Delete Division`
23. [Sesi A] Verifikasi toast sukses `Success, division has been deleted. Some items were skipped.`
24. [Sesi A] Verifikasi tidak ada pesan error (item yang berubah in-use di-skip tanpa error)
25. [Sesi A] Verifikasi Division `Internal Control {runId}-040` tetap ada di tabel
26. [Sesi A] Verifikasi Division `Research and Development {runId}-040` terhapus: baris hilang dari tabel
27. [Sesi A] Kosongkan isi kotak search lewat `(✕)`, tekan Enter

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Kelas harness: multi-konteks (dua admin), bagian 3 prinsip 13c.
- Subjudul `###` memetakan langkah ke id TC. Urutan di spec berbeda dari urutan sourceTc: TC-296 (tidak ada Division terhapus) ditaruh pertama, lalu TC-139 yang menghapus `Research and Development` (prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (pencarian `{runId}-040` supaya Division milik spec tampil), 13 (klik `[OK]` untuk menutup dialog blokir; TC sumber menyebutnya sebagai langkah "Setelah `[OK]`" pada butir c TC-296), 17 (membersihkan seleksi sebelum TC-139), 27 (membersihkan Search).
- Butir Expected TC-296 butir c ("Setelah `[OK]`: kedua baris tetap ada dan tetap tercentang; counter `2 Divisions selected`") dipecah menjadi langkah 14, 15, dan 16 setelah `[OK]` pada langkah 13. Butir b ("Tidak ada toast sukses maupun toast item dilewati") dipecah menjadi langkah 8 dan 9 yang diasersi tepat sesudah `[Delete]` (langkah 7) dan sebelum asersi isi dialog serta `[OK]`, karena toast adalah state sementara (bagian 8b butir 5).
- Butir Expected TC-139 diurutkan menurut state: toast ringkasan (butir c, langkah 23) diasersi tepat sesudah `[Delete]`, baru tidak ada pesan error (butir b, langkah 24) dan baris tabel (butir a, langkah 25 dan 26), karena toast adalah state sementara (bagian 8b butir 5). `Internal Control` tetap ada (langkah 25) sekaligus baris pembanding sebelum asersi `Research and Development` hilang (bagian 8b butir 2). TC-139 butir b ("di-skip tanpa error dan tanpa meng-crash batch") diasersi lewat tidak ada pesan error (langkah 24) dan batch selesai (R&D terhapus, langkah 26; toast ringkasan, langkah 23).
- Sesi B memakai sesi API pada kedua TC karena hanya memicu perubahan state (memindahkan atau menugaskan user ke Division) dan tidak ada asersi di Sesi B; objek asersi adalah hasil `[Delete]` Sesi A.
- Division memakai nama bersuffix `{runId}-040` (bukan nama literal) karena spec menghapus atau menjadikannya in-use dan asersi tidak bergantung pada nama literal. `Asal Uji {runId}-040` dibuat hanya sebagai Division awal user uji; spec tidak menyentuh Division Pre-setup sehingga relasi in-use mereka tidak berubah.
- Temuan untuk QA:
  - TC-296 langkah 2 ("Sesi Admin B memindahkan satu user ke `Audit Unit A` dan satu user lain ke `Audit Unit B`") dan TC-139 langkah 3 ("Admin lain menugaskan Division `Internal Control` ke sebuah user") tidak menyebut user target, Division awal user, maupun caranya (UI atau API). Spec memakai user uji milik spec; mekanisme disediakan tim FE.
  - TC-296 Post Condition ("Changelog dan Activity Log tanpa entri Delete baru") tidak punya langkah observasi di TC dan tidak diasersi; TC-296 tidak masuk spec absence.
  - TC-139 Post Condition ("Research and Development terhapus; Internal Control tetap") punya padanan di butir a.
  - Akun Admin B (Total Control kedua) tidak ada di Tabel Data Uji Pre-setup Division; disediakan tim FE.
