---
id: TC-GS-DIV-E2E-033-konflik-delete-in-use-saat-confirm-dan-sudah-dihapus
title: "Konflik Delete: Berubah In-Use Saat Confirm dan Sudah Dihapus Pihak Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-121
  - TC-GS-DIV-122
coverage:
  web: automated
---

# Konflik Delete: Berubah In-Use Saat Confirm dan Sudah Dihapus Pihak Lain

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin).
- Akun Sesi A (Admin A): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B): Total Control admin kedua (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`, pada entitas yang sama dengan Sesi A. Akun tidak tercantum di Tabel Data Uji Pre-setup Division; disediakan tim FE (akun yang sama dengan Admin B suite Brand).
- Sesi A berjalan di konteks browser dengan sesi login sendiri (seedSession di hook `before`, kredensial dari env var) dan berada di Global Settings > User > Division. Sesi B memakai sesi API (klien HTTP dengan kredensial Admin B; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (kemampuan seeding Division dan seeding User lewat API di hook `before`; tidak menumpang spec lain): `Security {runId}-033` (setara Security SEC, TC-GS-DIV-30; bebas relasi saat awal) dan `Strategy {runId}-033` (setara Strategy STR, TC-GS-DIV-30; bebas relasi). Satu user uji milik spec (Login User, nama dan email bersuffix `{runId}-033`; nilai field wajib lain disediakan tim FE) yang Division awalnya `Asal Uji {runId}-033`, sebuah Division milik spec yang dipakai user uji tersebut dan tidak diasersi. Code hasil seeding mengikuti auto-generate dan tidak diasersi.
- Kemampuan teknis: konteks browser Sesi A; klien HTTP untuk sesi API Sesi B; penugasan Division ke user oleh Sesi B (pemicu race TC-121; endpoint penugasan tidak disebut TC, PRD, atau LLD Division, disediakan tim FE); penghapusan Division oleh Sesi B lewat `DELETE /v2/iam/divisions` (TC-122); membaca request daftar Division (`POST /v2/iam/divisions/list`) untuk memastikan daftar di-refresh; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API user uji, lalu `Security {runId}-033`, `Strategy {runId}-033`, dan `Asal Uji {runId}-033` bila masih ada. Hook `beforeEach`: tutup dialog yang terbuka di Sesi A lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada (seluruh data milik spec dan dibersihkan).

## Test Steps

### Persiapan

1. [Sesi A] Ketik Search `{runId}-033`, tekan Enter

### TC-GS-DIV-121: Division berubah in-use di antara cek awal dan Confirm diblokir

2. [Sesi A] Buka row action baris `Security {runId}-033` lalu klik `Delete`
3. [Sesi B] Tugaskan Division `Security {runId}-033` ke user uji lewat sesi API
4. [Sesi A] Klik `[Delete]`
5. [Sesi A] Verifikasi tidak ada toast sukses
6. [Sesi A] Verifikasi dialog `Cannot Delete Data` tampil
7. [Sesi A] Verifikasi dialog memuat bullet `Security {runId}-033`
8. [Sesi A] Verifikasi dialog memuat tombol `[OK]`
9. [Sesi A] Klik `[OK]`
10. [Sesi A] Verifikasi Division `Security {runId}-033` tidak terhapus: baris tetap ada di tabel

### TC-GS-DIV-122: Delete Division yang sudah dihapus pihak lain berhasil tanpa error

11. [Sesi A] Buka row action baris `Strategy {runId}-033` lalu klik `Delete`
12. [Sesi B] Hapus Division `Strategy {runId}-033` lewat sesi API
13. [Sesi A] Klik `[Delete]`
14. [Sesi A] Verifikasi tidak ada pesan error
15. [Sesi A] Verifikasi toast sukses `Success, division has been deleted.`
16. [Sesi A] Verifikasi daftar di-refresh (request daftar Division dimuat ulang)
17. [Sesi A] Verifikasi baris `Security {runId}-033` tampil di tabel (pembanding)
18. [Sesi A] Verifikasi baris `Strategy {runId}-033` tidak ada di tabel
19. [Sesi A] Kosongkan isi kotak search lewat `(✕)`, tekan Enter

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Kelas harness: multi-konteks (dua admin), bagian 3 prinsip 13c.
- Subjudul `###` memetakan langkah ke id TC. Urutan TC mengikuti sourceTc: TC-121 tidak menghapus data dan TC-122 menghapus, sehingga aksi penghapusan sudah berada di akhir (prinsip 5).
- Butir Expected TC-121 diurutkan menurut state: "Tidak ada toast sukses" (butir c) diasersi segera sesudah pemicu `[Delete]` (langkah 5), sebelum asersi isi dialog dan sebelum `[OK]` ditutup, baru "Division tidak terhapus" (butir b) sesudah dialog ditutup (langkah 10), karena toast adalah state sementara (bagian 8b butir 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (pencarian `{runId}-033` supaya seluruh Division milik spec tampil; Search tidak diganti sampai langkah 19), 9 (klik `[OK]` untuk menutup dialog blokir; TC sumber tidak menyebutnya), 19 (membersihkan Search Sesi A).
- Asersi tambahan: langkah 17 (baris `Security {runId}-033` tampil) adalah baris pembanding sebelum asersi baris tidak ada (bagian 8b butir 2).
- Sesi B memakai sesi API pada kedua TC karena hanya memicu perubahan state (menugaskan Division ke user pada TC-121, menghapus Division pada TC-122) dan tidak ada asersi di Sesi B; objek asersi adalah hasil `[Delete]` Sesi A.
- Division memakai nama bersuffix `{runId}-033` (bukan nama literal Population D-02 `Security` dan `Strategy`) karena spec menghapus atau menjadikannya in-use dan asersi tidak bergantung pada nama literal.
- Temuan untuk QA:
  - TC-121 langkah 2 ("Admin B menugaskan Division `Security` ke sebuah user") tidak menyebut user target, Division awal user, maupun caranya (UI atau API). Spec memakai user uji milik spec dengan Division awal `Asal Uji {runId}-033`; mekanisme penugasan disediakan tim FE.
  - TC-121 tidak menyebut apakah Admin B bertindak lewat UI atau API; TC-122 menyebut "Admin B menghapus Division" tanpa cara. Spec memakai sesi API untuk keduanya.
  - TC-121 Post Condition ("Division Security tetap ada") punya padanan di butir b. TC-122 Post Condition ("Division Strategy terhapus") punya padanan di butir c.
  - Akun Admin B (Total Control kedua) tidak ada di Tabel Data Uji Pre-setup Division; disediakan tim FE.
