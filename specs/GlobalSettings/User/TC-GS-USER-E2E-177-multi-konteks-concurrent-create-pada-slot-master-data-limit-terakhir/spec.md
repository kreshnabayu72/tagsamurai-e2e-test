---
id: TC-GS-USER-E2E-177-multi-konteks-concurrent-create-pada-slot-master-data-limit-terakhir
title: "Multi-Konteks: Concurrent Create Dua Admin pada Slot Master Data Limit Terakhir"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-986
coverage:
  web: automated
---

# Multi-Konteks: Concurrent Create Dua Admin pada Slot Master Data Limit Terakhir

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Kelas harness: c (multi-konteks, dua sesi UI serentak), dengan kuota Master Data Count Limit sebagai pemicu state (P-2). Spec berjalan serial dalam suite (`parallel: false`) dan mengubah state global entitas Client Limit.
- Entitas uji: Client Limit, entitas khusus untuk kuota yang disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup No. 26). Entitas memuat Master Data Division `Finance` dan opsi Access `Fixed Asset`.
- Akun Sesi A (Admin A): Total Control pada entitas Client Limit, disediakan tim FE, kredensial `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Akun Sesi B (Admin B): Total Control admin kedua pada entitas Client Limit, disediakan tim FE, kredensial `Spectra.env.GS_LIMIT_TC2_PASSWORD`. Sesi B memakai konteks browser kedua (sesi UI) karena hasil di Sesi B (toast sukses atau dialog `Limit Reached`) diasersi; login di langkah eksplisit.
- Env var: `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` mengembalikan Sesi A ke Global Settings > User > User List, sub-tab Login User pada entitas Client Limit.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut mekanisme dan akunnya):
  - Mengatur Master Data Count Limit entitas Client Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits; pelaku dan cara (UI atau API) disediakan tim FE. Nilai awal dicatat dan dipulihkan di hook `after`.
  - Membaca jumlah Login + Non-Login User entitas Client Limit lewat API (disebut `N` di langkah).
  - Dua konteks browser dan klik `[Submit]` serentak di kedua sesi.
  - Klien HTTP untuk pembacaan API.
- Data Dinamis, semua bersuffix `{runId}-177`, Division `Finance`, Access `Fixed Asset`, Emergency Phone (No. 24, diisi mengikuti TC) Country Code `🇮🇩 +62` dan Number `81234567890`:
  - U-986a (Sesi A): First Name `Candra`, Last Name `Pertama {runId}-177`, Email `candrapertama+{runId}-177@qwertysystem.net`.
  - U-986b (Sesi B): First Name `Dewa`, Last Name `Kedua {runId}-177`, Email `dewakedua+{runId}-177@qwertysystem.net`.
- State global yang diubah: Master Data Count Limit entitas Client Limit (nilai awal dicatat dan dipulihkan), dan Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah.
- Cleanup di hook `after` (tidak berasumsi alur berhasil penuh): hapus lewat API seluruh user bersuffix `{runId}-177`, pulihkan Master Data Count Limit entitas Client Limit ke nilai awal, tutup konteks browser Sesi B beserta sesi loginnya, kembalikan sesi ke akun default suite.
- Nilai `N` dibaca ulang sebelum Master Data Count Limit diatur.

## Test Steps

### TC-GS-USER-986: Concurrent Create pada slot Master Data Limit terakhir

1. Baca jumlah Login + Non-Login User entitas Client Limit lewat API sebagai `N`
2. Atur Master Data Count Limit = `N` + 1
3. [Sesi B] Buka konteks browser kedua, login sebagai Admin B (`Spectra.env.GS_LIMIT_TC2_PASSWORD`)
4. [Sesi B] Klik menu User di sidebar Global Settings
5. [Sesi A] Klik `[+ User]` di Table Tools
6. [Sesi A] Isi First Name `Candra`, Last Name `Pertama {runId}-177`, Division `Finance`, Email `candrapertama+{runId}-177@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
7. [Sesi B] Klik `[+ User]` di Table Tools
8. [Sesi B] Isi First Name `Dewa`, Last Name `Kedua {runId}-177`, Division `Finance`, Email `dewakedua+{runId}-177@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
9. [Sesi A] dan [Sesi B] Klik `[Submit]` serentak
10. Verifikasi hanya satu user dibuat: jumlah Login + Non-Login User entitas Client Limit lewat API = `N` + 1
11. Verifikasi tepat satu sesi menampilkan toast sukses: "Success, user has been created."
12. Verifikasi sesi lainnya menampilkan dialog `Limit Reached`
13. [Sesi yang menampilkan dialog `Limit Reached`] Klik `[OK]`
14. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi Popup Create tetap terbuka
15. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi input dipertahankan: First Name, Last Name, Division, Email, dan Access sesuai yang diisi pada sesi itu
16. [Sesi yang menampilkan dialog `Limit Reached`] Klik `✕`
17. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi dialog `Unsaved Changes` tampil
18. [Sesi yang menampilkan dialog `Limit Reached`] Klik `[Leave]`
19. [Sesi B] Tutup konteks browser kedua dan hapus sesi loginnya

## Notes

- Mode: FE+BE. Kelas harness: c (multi-konteks). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-USER-986 berada di spec kelas c tersendiri karena dua sesi UI serentak tidak dicampur dengan kelas e (kuota).
- P-2 (pemicu bukan objek uji): kuota Master Data Count Limit (Master Data Count Limit = jumlah user + 1) hanya membentuk state slot terakhir; objek uji spec ini adalah balapan dua sesi UI (Sesi B menjadi objek asersi karena hasil di sesi itu diasersi). Spec multi-konteks (kelas c) ini tidak dipindah ke kelas e.
- TC-GS-USER-986 balapan: sesi mana yang diproses server lebih dulu tidak ditentukan (Sesi A atau Sesi B) dan spec tidak memaksanya. Karena itu langkah 11 dan 12 mengasersi hasil tanpa menamai sesi pemenang (tepat satu sesi dengan toast sukses, sesi lainnya dengan dialog `Limit Reached`), dan langkah 13 sampai 18 dijalankan pada sesi yang menampilkan dialog `Limit Reached`; tidak ada langkah bersyarat, karena Expected a menjamin tepat satu sesi seperti itu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 2 (membaca `N` dan mengatur limit), 3 sampai 4 (membuka Sesi B), 13 (menutup dialog `Limit Reached`), 16 sampai 18 (menutup form dirty sesi yang menampilkan dialog `Limit Reached`, S-08), 19 (menutup konteks Sesi B, S-09).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 17 (dialog `Unsaved Changes`) memenuhi penutupan form dirty yang deterministik (S-08).
- Temuan untuk QA:
  - TC-GS-USER-986: TC tidak menyebut sesi mana yang menang, cara melakukan Submit serentak, dan akun Admin B; spec menetapkan peran dari hasil teramati dan Admin B disediakan tim FE.
  - TC-GS-USER-986: precondition "System Limits = jumlah user + 1" tidak menyebut apakah Default User dan user Inactive dihitung; spec memakai jumlah Login + Non-Login User yang dibaca dari API.
  - TC-GS-USER-986 mengisi Emergency Phone (Pre-setup No. 24; Required nonaktif untuk TC ini) dengan Country Code `🇮🇩 +62` dan Number `81234567890`; spec mengikuti TC.
  - Akun Admin B (Sesi B) memakai admin kedua Client Limit (`GS_LIMIT_TC2_PASSWORD`), berbeda dari admin kedua Client A (`GS_TC2_PASSWORD`, spec 018); satu nama env satu arti (R-07).
