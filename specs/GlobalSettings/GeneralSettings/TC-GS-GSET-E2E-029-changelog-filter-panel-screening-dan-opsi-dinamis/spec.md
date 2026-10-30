---
id: TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis
title: "Modal Changelog: Screening Filter Panel dan Opsi Dropdown Filter Dinamis dari Data Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-71
  - TC-GS-GSET-72
  - TC-GS-GSET-75
  - TC-GS-GSET-150
  - TC-GS-GSET-174
coverage:
  web: automated
---

# Modal Changelog: Screening Filter Panel dan Opsi Dropdown Filter Dinamis dari Data Tabel

## Prerequisites

- Mode: FE+BE.
- Entitas: Client Satu Riwayat (Tabel Data Uji Pre-setup baris 25). Sebelum tiap run, entitas ini hanya memiliki satu baris Changelog (Field `Session Idle Timeout`, Modified By `Budi S`), dan Time Format tersimpan `HH:mm`. Pengembalian entitas ke keadaan itu (menghapus baris yang ditambah TC-GS-GSET-150) dilakukan tim FE/BE sebelum run lewat prosedur yang disediakan tim FE/BE; mekanismenya tidak tertulis di TC, PRD, atau LLD dan spec tidak mengarang endpoint (S-13). Changelog adalah audit trail permanen sehingga run kedua tanpa pengembalian gagal.
- Akun aktor: Total Control staf Client Satu Riwayat, Budi Santoso (`Budi S`). Email tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), password `Spectra.env.GS_ONEHIST_TC_PASSWORD` (nama env baru). Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Akun pelaku kedua lewat sesi API (tidak login UI, P-2): Total Control Client Satu Riwayat, Andi Wijaya (`Andi W`), email `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` entitas Client Satu Riwayat (Pre-setup baris 2 dan 25; disediakan tim FE), password `Spectra.env.GS_ONEHIST_TCB_PASSWORD` (nama env baru). Pendaftaran semua nama env baru di `spectra.config.ts` dan `.env.example` dilakukan pada tahap script.
- Environment variable: `GS_ONEHIST_TC_PASSWORD`, `GS_ONEHIST_TCB_PASSWORD`, `GS_TC_PASSWORD`.
- Aksi pelaku kedua (langkah 20): `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) oleh sesi API Andi Wijaya dengan `timeFormat` `hh:mm a` (nilai lain sama dengan nilai tersimpan entitas), payload mengacu ke `Fixture.generalSettings.payloadTimeFormat12h` (fixture belum ada; dibuat pada tahap script). Spec menunggu sampai perubahan tersimpan sebelum langkah berikutnya.
- Seeding lain: tidak ada. Dua baris Changelog yang dipakai TC-GS-GSET-174 (Budi Santoso dan Andi Wijaya masing-masing sedikitnya satu baris) terpenuhi oleh baris Pre-setup dan hasil langkah 20 (precondition TC, diasersi).
- Kemampuan teknis: membaca opsi dropdown filter; mengetik di kotak pencarian dalam dropdown.
- Changelog General Settings adalah audit trail permanen; asersi spec memakai pola nilai opsi dan baris, tidak pernah jumlah entri absolut (S-12).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Modal Changelog ditutup; sesi dikembalikan ke akun default suite. Baris Changelog yang ditambah langkah 20 tidak dapat dihapus; pengembalian entitas oleh tim FE/BE (lihat butir Entitas).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun Budi Santoso Client Satu Riwayat; spec ini tidak mengatur flag sendiri. Halaman General Settings dibuka di hook `beforeEach`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-71: Screening Filter Panel Changelog

1. Klik icon Changelog di pojok kanan atas halaman
2. Klik Filter di toolbar
3. Verifikasi Filter Panel memuat field Date bertipe date range picker dengan placeholder `Select date`
4. Verifikasi Filter Panel memuat field Field bertipe multi-select searchable dengan placeholder `All fields`
5. Verifikasi Filter Panel memuat field Modified By bertipe multi-select searchable dengan placeholder `All users`
6. Verifikasi Actions Filter Panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
7. Verifikasi tidak ada filter Action

### TC-GS-GSET-72: Opsi filter Field: populate dari baris Changelog entitas

8. Buka dropdown Field
9. Verifikasi dropdown Field hanya memuat opsi `Session Idle Timeout`
10. Verifikasi opsi `Currency Code`, `Time Zone`, `Date Format`, `Time Format`, dan `Currency Symbol` tidak tampil
11. Tutup dropdown Field

### TC-GS-GSET-75: Opsi filter Modified By: populate dari baris Changelog

12. Buka dropdown Modified By
13. Verifikasi dropdown Modified By hanya memuat opsi `Budi S`
14. Verifikasi opsi `Andi W` tidak tampil
15. Tutup dropdown Modified By

### TC-GS-GSET-150: Opsi filter Field dan Modified By bertambah setelah Save baru oleh admin lain tanpa reload

16. Buka dropdown Field
17. Verifikasi sebelum Save: dropdown Field hanya memuat opsi `Session Idle Timeout`
18. Tutup dropdown Field, lalu buka dropdown Modified By
19. Verifikasi sebelum Save: dropdown Modified By hanya memuat opsi `Budi S`
20. Admin B (Andi Wijaya, sesi API) memilih Time Format `hh:mm a` dan menyimpan hingga tersimpan
21. Tutup dropdown Modified By dan tutup Filter Panel, lalu klik Filter lagi pada Modal Changelog yang sama (tanpa reload halaman)
22. Buka dropdown Field
23. Verifikasi sesudah Save: dropdown Field memuat opsi `Session Idle Timeout` dan `Time Format`
24. Tutup dropdown Field, lalu buka dropdown Modified By
25. Verifikasi sesudah Save: dropdown Modified By memuat opsi `Budi S` dan `Andi W`
26. Tutup dropdown Modified By

### TC-GS-GSET-174: Dropdown filter Modified By: pencarian internal dan logika OR dalam satu field

27. Verifikasi placeholder field Modified By `All users`
28. Buka dropdown Modified By dan ketik `Andi` di kotak pencarian dropdown
29. Verifikasi opsi menyempit ke `Andi W`
30. Ganti isi kotak pencarian dropdown dengan `zzzz`
31. Verifikasi tidak ada opsi yang cocok
32. Kosongkan kotak pencarian dropdown, lalu centang `Budi S` dan `Andi W`
33. Verifikasi chip `Budi S` dan chip `Andi W` tampil di dalam field Modified By
34. Klik `[Apply]`
35. Verifikasi tabel menampilkan baris Modified By `Budi S` (baris Field `Session Idle Timeout`)
36. Verifikasi tabel menampilkan baris Modified By `Andi W` (baris Field `Time Format`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ukuran: 36 langkah, di atas smell sekitar 35 langkah (selisih satu langkah). Alasan pertahanan: satu kelas harness (Filter Panel Modal Changelog), satu entitas (Client Satu Riwayat), dan TC-174 bergantung pada baris yang ditambah TC-150 sehingga memisahkannya hanya menggandakan hook, login, dan pengembalian entitas.
- Urutan TC dalam spec: TC-71, 72, 75, 150, 174. Alasan: TC-71 adalah screening tanpa aksi; TC-72 dan 75 membaca opsi pada entitas yang hanya punya satu baris; TC-150 menambah baris oleh Admin B sehingga TC-174 (yang membutuhkan Budi Santoso dan Andi Wijaya masing-masing sedikitnya satu baris, dependensi TC-150) sesudahnya. Modal Changelog dan Filter Panel dibuka sekali di langkah 1 dan 2; langkah pembuka Changelog dan Filter pada TC-72, 75, dan 174 sudah terpenuhi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 15, 18, 21, 24, 26 (menutup dropdown atau Filter Panel agar dropdown berikutnya dapat dibuka; langkah 21 sekaligus aksi "menutup lalu membuka kembali Filter" pada TC-150 langkah 3) dan 32 (mengosongkan kotak pencarian dropdown sebelum mencentang opsi). Langkah 20 adalah pemicu TC-150 langkah 2 lewat sesi API (P-2: Admin B hanya memicu perubahan state; sesi UI kedua tidak diasersi).
- Langkah 17 dan 19 (nilai opsi sebelum Save pada TC-150) memuat asersi yang sama dengan langkah 9 dan 13 karena Expected TC-150 memintanya secara terpisah dari TC-72 dan 75 (S-01, S-04).
- Langkah 14 dan 10 adalah asersi absence atas opsi dropdown; anchor positif tiap langkah adalah `Verifikasi` opsi yang tampil pada dropdown yang sama (langkah 9 dan 13, bagian 8b butir 2).
- Langkah 35 dan 36 memetakan Expected e TC-174 ("baris Modified By `Budi S` ATAU `Andi W`"); baris dikenali lewat Field karena Budi S menghasilkan baris Field `Session Idle Timeout` (Pre-setup 25) dan Andi W baris Field `Time Format` (langkah 20).
- Temuan untuk QA:
  - TC-GS-GSET-72, 75, 150, 174 (Q-06): Client Satu Riwayat harus tepat satu baris Changelog di awal, tetapi TC-150 menambah baris oleh Admin B sehingga run kedua gagal tanpa pengembalian entitas; mekanisme pengembalian tidak ada di TC, PRD, atau LLD dan disediakan tim FE/BE.
  - Email akun Budi Santoso staf Client Satu Riwayat tidak tertulis di Pre-setup TC (baris 25 hanya menyebut nama dan Andi Wijaya "entitas yang sama"); akun disediakan tim FE.
  - TC-GS-GSET-150 langkah 2 menyebut Admin B "memilih Time Format `hh:mm a` dan klik `[Save]`" di UI dan precondition d menyebut Admin B berada di halaman; sesuai konvensi pelaku kedua yang hanya memicu perubahan state memakai sesi API, sehingga pemicu ditulis "hingga tersimpan" lewat PUT.
  - TC-GS-GSET-150 mengasumsikan Time Format tersimpan entitas bukan `hh:mm a` pada awal run; nilai awal tidak tertulis di Pre-setup baris 25.
  - TC-GS-GSET-75 b menyebut `Andi W` belum pernah Save, sedangkan TC-174 precondition d ("masing-masing punya sedikitnya 1 baris") hanya benar sesudah TC-150; urutan spec mengikuti dependensi TC-150.
