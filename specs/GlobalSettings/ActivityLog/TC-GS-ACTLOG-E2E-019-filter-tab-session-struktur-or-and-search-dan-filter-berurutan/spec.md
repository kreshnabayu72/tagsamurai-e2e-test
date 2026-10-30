---
id: TC-GS-ACTLOG-E2E-019-filter-tab-session-struktur-or-and-search-dan-filter-berurutan
title: "Filter Tab Session: Struktur, OR, AND, Search dan Filter Berurutan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-66
  - TC-GS-ACTLOG-67
  - TC-GS-ACTLOG-70
  - TC-GS-ACTLOG-71
  - TC-GS-ACTLOG-72
  - TC-GS-ACTLOG-73
coverage:
  web: automated
---

# Filter Tab Session: Struktur, OR, AND, Search dan Filter Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: tiga user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Password aksi subjek: Login dengan password salah memakai `Spectra.env.LP_PASSWORD_WRONG`; Change Password Budi memakai password lama `Spectra.env.ACTLOG_PASSWORD` dan password baru `Spectra.env.ACTLOG_PASSWORD_NEW` (env baru, didaftarkan di tempat yang sama). Urutan di hook `before`: Login password salah Budi lebih dulu, lalu Change Password Budi (password Budi menjadi `ACTLOG_PASSWORD_NEW`). Tidak ada login Budi sesudahnya.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-019`, `{runId}` hanya digit; nama opsi User di Filter Panel adalah nama lengkap):

  | Subjek | First Name | Last Name | Email | Position | Division | Tampil di kolom User |
  |---|---|---|---|---|---|---|
  | John | `John` | `Doe {runId}-019` | `Fixture.activityLog.john019.email` (ditetapkan tim FE, fixture baru) | `Staff {runId}-019` | `Marketing {runId}-019` | `John D` |
  | Budi | `Budi` | `Anwar {runId}-019` | `Fixture.activityLog.budi019.email` (ditetapkan tim FE, fixture baru) | `Supervisor {runId}-019` | `Finance {runId}-019` | `Budi A` |
  | Siti | `Siti` | `Nurbaya {runId}-019` | `Fixture.activityLog.siti019.email` (ditetapkan tim FE, fixture baru) | tanpa Position | `Operations {runId}-019` | `Siti N` |

- Data log subjek (entri Session):

  | Subjek | Activity | Status tampil | Note | Cara |
  |---|---|---|---|---|
  | John | Login | `Success` | `Login with password` | Aksi nyata: Login dengan password benar |
  | John | Logout | `—` | `Logged out` | Aksi nyata: Logout manual |
  | John | Session | `—` | `Session started` | Aksi nyata: buka card Global Settings |
  | Budi | Login | `Failed` | `Incorrect password` | Aksi nyata: Login dengan password salah |
  | Budi | Reset Password | `Failed` | `Too many reset attempts` | Seed BE |
  | Budi | Change Password | `Success` | `Password changed` | Aksi nyata: Change Password di My Profile dengan password lama benar |
  | Siti | Reset Password | `Success` | `Password reset requested` | Aksi nyata: permintaan Reset Password dari halaman Login |

- Data uji TC-GS-ACTLOG-67 (dua opsi per field, logika OR dalam satu field):

  | Field | Opsi dipilih | Baris subjek yang tampil | Baris subjek yang tidak tampil |
  |---|---|---|---|
  | User | `John Doe {runId}-019` dan `Siti Nurbaya {runId}-019` | semua baris milik John dan Siti | semua baris milik Budi |
  | Position | `Staff {runId}-019` dan `Supervisor {runId}-019` | semua baris milik John dan Budi | semua baris milik Siti (tanpa Position) |
  | Division | `Marketing {runId}-019` dan `Operations {runId}-019` | semua baris milik John dan Siti | semua baris milik Budi (Division Finance) |
  | Activity | `Login` dan `Logout` | baris Login John, Login Budi, dan Logout John | baris Reset Password (Budi dan Siti), Change Password Budi, dan Session John |
  | Status | `Success` dan `Failed` | baris dengan Status tampil `Success` atau `Failed` (Login John, Login Budi, Reset Password Budi, Reset Password Siti, Change Password Budi) | baris dengan Status tampil `—` (Logout John, Session John) |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Reset Password `Failed` Note `Too many reset attempts` (tidak dapat dibentuk dari aksi penguji; tanpa mengarang endpoint); menjalankan aksi Auth dan My Profile sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- State global: Search dan Filter tab Session dikosongkan di akhir spec (langkah 52 sampai 54). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga user subjek beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-66: Struktur Filter Panel Tab Session, 6 field

2. Klik icon Filter
3. Verifikasi field di Filter Panel berurutan dari atas ke bawah: `Date`, `User`, `Position`, `Division`, `Activity`, `Status`
4. Verifikasi field `Date` berupa date range picker
5. Verifikasi field `Date` memiliki placeholder `Select date`
6. Verifikasi field `User` berupa multi-select searchable
7. Verifikasi field `User` memiliki placeholder `All users`
8. Verifikasi field `Position` berupa multi-select searchable
9. Verifikasi field `Position` memiliki placeholder `All positions`
10. Verifikasi field `Division` berupa multi-select searchable
11. Verifikasi field `Division` memiliki placeholder `All divisions`
12. Verifikasi field `Activity` berupa multi-select searchable
13. Verifikasi field `Activity` memiliki placeholder `All activities`
14. Verifikasi field `Status` berupa multi-select searchable
15. Verifikasi field `Status` memiliki placeholder `All statuses`
16. Verifikasi tombol footer panel `[Clear Field]` di kiri dan `[Apply]` di kanan
17. Verifikasi icon Filter di toolbar berubah gelap saat panel terbuka

### TC-GS-ACTLOG-67: Filter multi-select, dua opsi dalam satu field memakai logika OR

18. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-67 (langkah 18 sampai 23): klik icon Filter, lalu pilih dua opsi pada field
19. Klik `[Apply]`
20. Verifikasi tabel menampilkan baris subjek pada kolom "Baris subjek yang tampil"
21. Verifikasi baris subjek pada kolom "Baris subjek yang tidak tampil" tidak tampil
22. Klik `[Clear Field]`
23. Klik `[Apply]`

### TC-GS-ACTLOG-70: Filter dua field berbeda memakai logika AND

24. Klik icon Filter, lalu pilih Activity `Login` dan Status `Failed`
25. Klik `[Apply]`
26. Verifikasi baris Login `Failed` milik Budi tampil
27. Verifikasi baris Login `Success` milik John dan baris Reset Password `Failed` milik Budi tidak tampil

### Pemulihan state antar TC

28. Klik `[Clear Field]`
29. Klik `[Apply]`

### TC-GS-ACTLOG-71: OR dalam satu field dan AND antar field dalam satu penerapan

30. Klik icon Filter, lalu pilih Activity `Login` dan `Reset Password`, dan pilih Status `Failed`
31. Klik `[Apply]`
32. Verifikasi baris Login `Failed` dan Reset Password `Failed` milik Budi tampil
33. Verifikasi baris Login `Success` milik John, Reset Password `Success` milik Siti, dan Logout milik John tidak tampil

### Pemulihan state antar TC

34. Klik `[Clear Field]`
35. Klik `[Apply]`

### TC-GS-ACTLOG-72: Alur Search lalu Filter

36. Ketik Search `Budi`, tekan Enter
37. Klik icon Filter, lalu pilih Activity `Login`
38. Klik `[Apply]`
39. Verifikasi baris Login milik Budi tampil
40. Verifikasi baris Change Password milik Budi dan baris Login milik John tidak tampil
41. Verifikasi kata kunci `Budi` tetap ada di kotak Search setelah Filter diterapkan

### Pemulihan state antar TC

42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-GS-ACTLOG-73: Alur Filter lalu Search

45. Klik icon Filter, lalu pilih Activity `Login`
46. Klik `[Apply]`
47. Ketik Search `Budi`, tekan Enter
48. Verifikasi baris Login milik Budi tampil
49. Verifikasi baris Change Password milik Budi dan baris Login milik John tidak tampil
50. Klik icon Filter
51. Verifikasi Filter Panel masih memuat Activity `Login` terpilih

### Pemulihan state akhir

52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Filter Panel Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-68 dan 69 (bergantung pada TC-GS-ACTLOG-66) ada di spec 020, TC-GS-ACTLOG-78, 81, dan 82 di spec 021, serta TC-GS-ACTLOG-83, 84, dan 85 di spec 022. TC-GS-ACTLOG-72 bergantung pada TC-GS-ACTLOG-58 yang ada di spec 017.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 28, 34, dan 42 (masing-masing `[Clear Field]` diikuti `[Apply]`; langkah 44 menutup Search) untuk membersihkan Filter dan Search sebelum TC berikutnya serta langkah 52 sampai 54 (membersihkan state di akhir spec; hook `after` sebagai cadangan). Langkah 3 sampai 17 memetakan satu butir Expected (a, b, c) menjadi beberapa `Verifikasi` per klausa (S-01): tipe kontrol dan placeholder tiap field dipisah.
- Langkah 18 sampai 23 berulang untuk setiap baris tabel Data uji TC-GS-ACTLOG-67 di Prerequisites.
- Spec memiliki 54 langkah nominal dan 78 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok memakai Filter Panel Tab Session, akun, dan dataset yang sama; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sebagian langkah adalah `Verifikasi` hasil pemecahan klausa Expected (S-01) dan langkah pemulihan antar TC.
- Temuan untuk QA:
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 18, 24, 30, 37, 45, dan 50 mengikuti TC-GS-ACTLOG-67, 70, 71, 72, dan 73.
  - Perilaku `[Apply]` pada Filter Panel (panel menutup atau tetap terbuka) belum ditetapkan PRD dan TC saling tidak konsisten: TC-GS-ACTLOG-66 berakhir dengan panel terbuka, tetapi TC-GS-ACTLOG-67 langkah 1 dimulai dengan klik icon Filter; TC-GS-ACTLOG-67 menekan `[Clear Field]` dan `[Apply]` tepat sesudah `[Apply]` tanpa membuka ulang panel, sedangkan TC-GS-ACTLOG-70 sampai 73 mengawali langkah dengan klik icon Filter; TC-GS-ACTLOG-73 langkah 2 "amati Filter Panel" tidak menyatakan keadaan panel. Spec mengikuti urutan langkah TC apa adanya (klik icon Filter di langkah 18, 24, 30, 37, 45, dan 50; `[Clear Field]` tanpa membuka ulang di langkah 28, 34, 42, dan 52).
  - Tabel Tab Session entitas Client A memuat log dari spec dan run lain, sedangkan Expected TC ("hanya baris ... tampil") ditulis seolah hanya data TC yang ada. Semua asersi dibatasi pada baris subjek spec ini (nama bersuffix); Search `Budi` pada TC-GS-ACTLOG-72 dan 73 juga cocok dengan subjek `Budi` milik spec lain.
  - Nama subjek literal TC (`John Doe`, `Budi Anwar`, `Siti Nurbaya`) diganti nama bersuffix per run (S-12); singkatan `John D`, `Budi A`, `Siti N` tetap sama. Entri Reset Password `Failed` tidak dapat dibentuk dari aksi penguji sehingga dicatat sebagai seed BE.
  - Env baru: `ACTLOG_PASSWORD` dan `ACTLOG_PASSWORD_NEW` belum ada di `.env.example` dan perlu didaftarkan tim FE.
