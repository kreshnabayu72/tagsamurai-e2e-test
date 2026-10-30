---
id: TC-GS-ACTLOG-E2E-038-aksi-lain-user-action-permission-system-role-activate-dan-import
title: "Aksi Lain di User Action: Edit Permission System Role, Activate/Deactivate, Import"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-146
  - TC-GS-ACTLOG-147
  - TC-GS-ACTLOG-149
coverage:
  web: automated
---

# Aksi Lain di User Action: Edit Permission System Role, Activate/Deactivate, Import

## Prerequisites

- Mode: FE+BE.
- Akun pembaca log: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku aksi sumber (sesi API, fixture baru): Admin `Hendra Pratama` (`Fixture.activityLog.adminHendra`, email ditetapkan tim FE, kredensial `Spectra.env.GS_HENDRA_PASSWORD`, env baru). Sesi API dibuka di hook `before` dan ditutup di hook `after`. Admin ini melakukan semua aksi sumber.
- Data Dinamis (bersuffix `{runId}-038`, di-seed lewat API di hook `before`):
  - System Role `Role Uji {runId}-038` dengan satu permission `Fixture.activityLog.permissionUji` (fixture baru: nama permission pada modul Role & Permission) berstatus `Inactive`.
  - User `Jane Smith {runId}-038` (email `janesmith+{runId}-038@qwertysystem.net`) dalam status Inactive sebelum diaktifkan.
  - Berkas Import `Fixture.activityLog.berkasImport` (fixture baru; baris di dalamnya bernama bersuffix `{runId}-038`).
  - Nilai field wajib lain user dari `Fixture.activityLog.userDasar` (fixture baru berisi Position, Employee ID, dan field wajib lain di luar Name, email, dan Division).
- Kemampuan teknis (disediakan tim FE/BE): aksi sumber (aktifkan permission System Role di modul Role & Permission, Activate dan Deactivate user di modul User, Import massal dari modul Import) dijalankan lewat sesi API admin; Changelog modul sumber dapat dibaca dari UI Total Control Client A untuk perbandingan.
- Guided Tooltip: hook suite before/after menyetel flag seen untuk halaman Activity Log (lihat suite.md). Hook before/after spec ini juga menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman Changelog modul Role & Permission dan User yang dibuka pada langkah 4 dan 11 (kemampuan disediakan tim FE/BE).
- Cara baca jumlah baris (langkah 15 dan 18): PRD tidak punya indikator total baris, sehingga yang dihitung adalah baris yang tampil. Klik menu Activity Log di sidebar mengembalikan ukuran halaman ke default 10 (PRD FI-06), sehingga langkah 15 dan 17 mengatur jumlah baris per halaman ke 100 (pilihan 10/25/50/100) sebagai aksi sebelum baris dibaca; ukuran halaman setelah [Apply] tidak ditetapkan PRD. Hasil dipersempit dengan Filter Action `Import`, Modified By `Hendra Pratama`, dan Date hari ini supaya jumlah baris hasil kurang dari satu halaman. Entri log tidak dapat dihapus; asersi memakai selisih jumlah baris sehingga tahan baris dari run lain.
- Entri awal (hook `before`, sebelum langkah 15): satu Import massal lewat sesi API admin Hendra Pratama dengan `Fixture.activityLog.berkasImportAwal` (fixture baru, disediakan tim FE; baris bernama bersufiks `{runId}-038`), sehingga opsi Action `Import` ada di Filter Panel dan baseline B149 dapat diambil.
- State global yang diubah: tidak ada selain data milik spec. Hook `after` menghapus System Role, user, dan data hasil Import milik spec ini; entri log tidak dapat dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-146: Edit permission System Role tercatat identik dengan Changelog modul sumber

1. Sebagai admin Hendra Pratama (sesi API), aktifkan permission `Fixture.activityLog.permissionUji` pada System Role `Role Uji {runId}-038` (nilai berubah dari `Inactive` menjadi `Active`)
2. Buka Global Settings > Activity Log > Tab "User Action", ketik Search `Role Uji {runId}-038`, tekan Enter
3. Verifikasi entri Action `Edit` dengan Object `System Role` tampil
4. Catat Object, Name, Field, Old Value, dan New Value entri itu, lalu buka Changelog modul Role & Permission dan baca baris Edit untuk perubahan permission itu
5. Verifikasi Object, Name, Field, Old Value (`Inactive`), dan New Value (`Active`) entri itu identik dengan baris Changelog modul sumber untuk aksi yang sama

### Pemulihan state antar TC

6. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-147: Aksi perubahan status, Activate dan Deactivate user

7. Sebagai admin Hendra Pratama (sesi API), aktifkan user `Jane Smith {runId}-038` secara global di modul User, lalu nonaktifkan user yang sama
8. Ketik Search `Jane Smith {runId}-038`, tekan Enter
9. Verifikasi entri Action `Activate` dengan Object `User` tampil
10. Verifikasi entri Action `Deactivate` dengan Object `User` tampil
11. Catat Object, Name, Field, Old Value, dan New Value kedua entri, lalu buka Changelog user `Jane Smith {runId}-038` di modul User dan baca baris Activate dan Deactivate
12. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Activate` identik dengan baris Changelog modul sumber untuk aksi yang sama
13. Verifikasi Object, Name, Field, Old Value, dan New Value entri `Deactivate` identik dengan baris Changelog modul sumber untuk aksi yang sama

### Pemulihan state antar TC

14. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default, lalu klik tab "User Action"

### TC-GS-ACTLOG-149: Entri Import, Name kosong untuk aksi massal

15. Pada Tab "User Action" klik icon Filter, pilih Action `Import`, Modified By `Hendra Pratama`, dan Date hari ini, klik [Apply], atur jumlah baris per halaman ke 100, lalu hitung baris yang tampil sebagai baseline B149
16. Sebagai admin Hendra Pratama (sesi API), jalankan Import massal dari modul Import dengan berkas `Fixture.activityLog.berkasImport`
17. Klik icon Filter, klik [Apply] untuk memuat ulang hasil Filter, lalu atur jumlah baris per halaman ke 100
18. Verifikasi jumlah baris yang tampil pada hasil Filter (ukuran halaman 100) bertambah satu dari B149 dan seluruh baris hasil Filter menampilkan Action `Import` (posisi baris tidak diasersi karena yang diverifikasi adalah jumlah dan Action seluruh baris hasil Filter)
19. Verifikasi kolom Name tampil `—` pada seluruh baris Action `Import` hasil Filter (baris tidak ditunjuk satu per satu karena Import massal tidak punya Name dan semua baris Import hasil Filter ber-Action `Import`)

### Pemulihan state akhir

20. Klik icon Filter, klik [Clear Field], klik [Apply]

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-146, 147, 149 dipertahankan.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 7, dan 16 (aksi sumber oleh admin lewat sesi API), langkah 4 dan 11 (mencatat nilai entri lalu membaca Changelog modul sumber sebagai pembanding), langkah 15 (baseline jumlah baris sesuai S-12), langkah 17 (memuat ulang hasil Filter), dan langkah pemulihan 6, 14, dan 20.
- Klausa "entri tampil" dan "kolom identik dengan Changelog" dipisah (S-01); kolom satu entri dijadikan satu `Verifikasi` karena daftarnya disebut utuh.
- Entri dicari lewat Search Name bersuffix (baseline nol, S-12). Entri Import bernama `—` sehingga dicari lewat Filter Action `Import` dengan baseline jumlah baris. Import massal lewat sesi API selesai sinkron sehingga tidak memakai langkah tunggu aksi.
- Activity Log dibuka kembali lewat menu sidebar (state default) sesudah mengunjungi modul lain, dan Search diketik ulang.
- Temuan untuk QA:
  - State kotak Search saat user keluar dari halaman Activity Log lalu kembali belum ditetapkan PRD; spec tidak mengandalkannya.
  - Env baru `GS_HENDRA_PASSWORD` perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; email dan role admin Hendra Pratama ditetapkan tim FE.
  - TC-146 menyebut permission aktif pada "System Role milik user `Siti Nurbaya`", tetapi tidak menyebut permission mana dan modul pengubahnya; spec memakai System Role uji dan permission dari fixture baru.
  - TC-146 tidak menyebut kolom Name entri Edit System Role (bisa nama role atau nama user pemegang role); spec mencari lewat nama role uji bersuffix dan asersi Name mengikuti Changelog modul sumber (asumsi). Bila Name ternyata nama user pemegang role, pencarian langkah 2 perlu nama yang dikonfirmasi tim FE/BE. Spec tidak men-seed user pemegang System Role.
  - TC-149 menulis entri `Import` tampil tanpa cara menghitung jumlah baris pada tabel berpaginasi dan PRD Activity Log tidak punya indikator total; spec menghitung baris yang tampil pada ukuran halaman 100 setelah hasil dipersempit (pilihan spec; pemilik TC dan PRD perlu menetapkan cara baca atau indikator total).
  - TC-147 tidak menyebut status awal `Jane Smith`; spec memakai status Inactive agar urutan Activate lalu Deactivate valid.
  - TC-149 tidak menyebut berkas Import maupun modul Import secara rinci; kebutuhannya dicatat di Prerequisites sebagai fixture baru.
  - TC-146, 147, dan 149 memakai aktor Admin yang tidak dinamai; spec memakai Admin `Hendra Pratama`.
  - Ukuran halaman tabel sesudah [Apply] belum ditetapkan PRD (klik menu sidebar mengembalikan ke 10, FI-06); spec mengatur 100 sebagai aksi pada langkah 15 dan 17.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah 17 dan 20 mengikuti pola TC.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
