---
id: TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql
title: "Defense-in-Depth: Request Langsung Tanpa Capability, Guard In-Use, Validasi Server, XSS, dan SQL Injection"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-259
  - TC-GS-DIV-260
  - TC-GS-DIV-261
  - TC-GS-DIV-262
  - TC-GS-DIV-267
  - TC-GS-DIV-268
  - TC-GS-DIV-269
  - TC-GS-DIV-270
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Tanpa Capability, Guard In-Use, Validasi Server, XSS, dan SQL Injection

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai empat akun dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Read Only (Maya Putri) | `readOnly_automated_qaTeam1@qwertysystem.net` | `GS_RO_PASSWORD` |
  | 2 | System Role Create+Read (Rina Marlina) | `createOnly_automated_qaTeam1@qwertysystem.net` | `GS_CREATE_PASSWORD` |
  | 3 | System Role Update+Read (Agus Wijaya) | `updateOnly_automated_qaTeam1@qwertysystem.net` | `GS_UPDATE_PASSWORD` |
  | 4 | Total Control (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun 4). Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_RO_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup dan Population D-02 tidak dipakai dan tidak diubah; seluruh target request tulis atau hapus langsung ke server adalah Division milik spec.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh data milik spec ini), di-seed lewat API (kemampuan seeding Division dan Login User lewat API) di hook `before` oleh akun Total Control, Code di-generate otomatis:
  - `Finance {runId}-073`: Division bebas relasi, target request Edit pada TC-GS-DIV-260, target request Delete pada TC-GS-DIV-261, dan target Edit lewat UI pada TC-GS-DIV-270 (setara `Finance` pada TC).
  - `Human Resources {runId}-073`: Division in-use oleh Login User aktif uji `inuse+{runId}-073@qwertysystem.net` (di-seed lewat API di hook `before`; nilai field wajib lain disediakan tim FE lewat fixture `fixtures/division.json` yang belum ada), target request Delete in-use pada TC-GS-DIV-262 (setara `Human Resources` pada TC).
  - `<script>alert(1)</script> {runId}-073` dengan Code `XSS1`, dibuat spec lewat UI pada TC-GS-DIV-268. Nama bersuffix per run dan nomor spec, markup tetap literal; Code `XSS1` dipakai sesuai TC (pengecualian S-12: cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial).
  - Input uji `Bypass Create` (TC-GS-DIV-259), `Finance Bypass {runId}-073` (Name baru pada request Edit TC-GS-DIV-260), dan `Finance 😀` (TC-GS-DIV-267 dan 270) adalah input yang ditolak sehingga tidak membuat data.
- Cleanup (hook `after`, tidak berasumsi langkah spec berhasil penuh): hapus lewat API Login User `inuse+{runId}-073@qwertysystem.net`, lalu Division `Finance {runId}-073` (atau `Finance Bypass {runId}-073` atau `Finance 😀` bila Name berubah), `Human Resources {runId}-073`, `Bypass Create`, `Finance 😀`, dan `<script>alert(1)</script> {runId}-073` bila ada. Hook `before` menghapus lewat API sisa Division bernama `<script>alert(1)</script> {runId lama}-073` (nama berpola `<script>alert(1)</script> *-073`, bukan berdasarkan Code saja) yang masih memegang Code `XSS1`.
- Kemampuan teknis: (a) klien HTTP yang mengirim request Create, Edit, dan Delete Division langsung ke server dengan token sesi akun yang sedang login, tanpa lewat UI (endpoint dan cara menangkap token disediakan tim FE); (b) menyetel nilai field Division Name langsung lewat DOM, melewati validasi klien, untuk TC-GS-DIV-267 dan 270; (c) mendeteksi eksekusi skrip dan dialog browser selama halaman diamati, untuk TC-GS-DIV-268; (d) seeding Division dan Login User serta penghapusannya lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Tidak ada state global yang diubah.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- TC-GS-DIV-259: login sebagai Read Only. TC-GS-DIV-260: Create+Read. TC-GS-DIV-261: Update+Read. TC-GS-DIV-262, 267, 268, 269, 270: Total Control. Semua berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-259: Request Create langsung tanpa capability Create ditolak server

1. Tangkap token sesi Read Only, lalu kirim request Create Division dengan Name `Bypass Create` langsung ke server tanpa lewat UI
2. Verifikasi server menolak dengan `403 Forbidden`
3. Ketik Search `Finance {runId}-073`, tekan Enter pada tabel Division
4. Verifikasi Division `Finance {runId}-073` tampil di tabel
5. Ganti isi kotak search dengan `Bypass Create`, tekan Enter
6. Verifikasi Division `Bypass Create` tidak dibuat (tidak ada di tabel)

### TC-GS-DIV-260: Request Edit langsung tanpa capability Update ditolak server

7. Logout, lalu login sebagai System Role Create+Read (`createOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_CREATE_PASSWORD`
8. Buka Global Settings > User > Division
9. Tangkap token sesi Create+Read, lalu kirim request Edit Division `Finance {runId}-073` dengan Name baru `Finance Bypass {runId}-073` langsung ke server
10. Verifikasi server menolak dengan `403 Forbidden`
11. Ketik Search `{runId}-073`, tekan Enter pada tabel Division
12. Verifikasi Name `Finance {runId}-073` tidak berubah (baris `Finance {runId}-073` tetap ada)
13. Verifikasi Division `Finance Bypass {runId}-073` tidak ada di tabel

### TC-GS-DIV-261: Request Delete langsung tanpa capability Delete ditolak server

14. Logout, lalu login sebagai System Role Update+Read (`updateOnly_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_UPDATE_PASSWORD`
15. Buka Global Settings > User > Division
16. Tangkap token sesi Update+Read, lalu kirim request Delete Division `Finance {runId}-073` langsung ke server
17. Verifikasi server menolak dengan `403 Forbidden`
18. Ketik Search `Finance {runId}-073`, tekan Enter pada tabel Division
19. Verifikasi Division `Finance {runId}-073` tetap ada di tabel

### TC-GS-DIV-262: Request Delete Division in-use langsung ke server tetap ditolak guard

20. Logout, lalu login sebagai Total Control (`totalControl_automated_qaTeam1@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`
21. Buka Global Settings > User > Division
22. Tangkap token sesi Total Control, lalu kirim request Delete Division `Human Resources {runId}-073` langsung ke server tanpa lewat UI
23. Verifikasi server menolak penghapusan karena Division masih dipakai user
24. Ketik Search `Human Resources {runId}-073`, tekan Enter pada tabel Division
25. Verifikasi Division `Human Resources {runId}-073` tetap ada di tabel

### TC-GS-DIV-269: Search berisi payload SQL tidak memengaruhi hasil

26. Ganti isi kotak search dengan `' OR '1'='1`, tekan Enter pada tabel Division
27. Verifikasi tidak ada toast error atau pesan error server
28. Verifikasi tabel menampilkan `No results found`
29. Verifikasi tidak ada baris Division yang tampil (tidak ada data bocor)
30. Klik `(←)` pada kotak Search

### TC-GS-DIV-270: Edit Name berisi emoji yang lolos validasi klien tetap ditolak server

31. Ketik Search `Finance {runId}-073`, tekan Enter
32. Klik `⋯` pada baris `Finance {runId}-073` > Edit
33. Injeksi value `Finance 😀` langsung ke DOM field Division Name (melewati validasi klien)
34. Klik [Save]
35. Verifikasi modal Edit tetap terbuka
36. Verifikasi input `Finance 😀` dipertahankan di field Division Name
37. Verifikasi penolakan server ditampilkan pada form
38. Klik `✕` pada form Edit Division
39. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
40. Klik `[Leave]`
41. Ganti isi kotak search dengan `Finance`, tekan Enter
42. Verifikasi Name tetap `Finance {runId}-073` (baris `Finance {runId}-073` tampil di tabel)
43. Verifikasi Division `Finance 😀` tidak ada di tabel
44. Klik `(←)` pada kotak Search

### TC-GS-DIV-267: Name berisi emoji yang lolos validasi klien tetap ditolak server

45. Klik `[+ Division]`
46. Injeksi value `Finance 😀` langsung ke DOM field Division Name (melewati validasi klien)
47. Klik [Submit]
48. Verifikasi modal Create tetap terbuka
49. Verifikasi input `Finance 😀` dipertahankan di field Division Name
50. Verifikasi penolakan server ditampilkan pada form
51. Klik `✕` pada form Create Division
52. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
53. Klik `[Leave]`
54. Ketik Search `Finance`, tekan Enter
55. Verifikasi Division `Finance {runId}-073` tampil di tabel
56. Verifikasi Division `Finance 😀` tidak dibuat (tidak ada di tabel)
57. Klik `(←)` pada kotak Search

### TC-GS-DIV-268: Division Name berisi markup HTML ditampilkan sebagai teks biasa

58. Klik `[+ Division]`, isi Division Name `<script>alert(1)</script> {runId}-073` dan Code `XSS1`, lalu klik [Submit]
59. Tunggu aksi selesai
60. Ketik Search `<script>alert(1)</script> {runId}-073`, tekan Enter
61. Verifikasi Name tampil sebagai teks literal `<script>alert(1)</script> {runId}-073` di baris tabel
62. Klik `⋯` pada baris tersebut > Delete
63. Verifikasi Name tampil sebagai teks literal `<script>alert(1)</script> {runId}-073` di dialog `Delete Division`
64. Klik `[Cancel]` pada dialog `Delete Division`
65. Klik icon `[Changelog]` pada toolbar
66. Ketik Search `<script>alert(1)</script> {runId}-073`, tekan Enter pada Modal Changelog
67. Verifikasi Name tampil sebagai teks literal `<script>alert(1)</script> {runId}-073` di Modal Changelog
68. Verifikasi tidak ada skrip yang dieksekusi di tabel, dialog hapus, dan Modal Changelog
69. Verifikasi tidak ada dialog browser yang tampil
70. Tutup Modal Changelog lewat `✕`
71. Klik `(←)` pada kotak Search tabel Division

## Notes

- Sumber: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas defense-in-depth (prinsip 13a) tanpa harness eksternal.
- Urutan TC di spec berbeda dari urutan sumber: akun diurutkan Read Only (259), Create+Read (260), Update+Read (261), lalu Total Control untuk sisanya (262, 269, 270, 267, 268) dengan tiga kali ganti akun eksplisit (langkah 7, 14, 20). Di bagian Total Control: aksi tanpa data baru lebih dulu (262, 269), validasi diblokir (270 lalu 267), dan aksi yang membuat data paling akhir (268), sesuai bagian 3 konvensi.
- Target request tulis dan hapus langsung ke server serta Edit lewat UI adalah Division milik spec (`Finance {runId}-073`, `Human Resources {runId}-073`; S-06); TC menulis `Finance` dan `Human Resources` dan Division Pre-setup tidak disentuh spec ini.
- Request langsung ke server (TC-GS-DIV-259, 260, 261, 262): asersi hanya respons server dan state data lewat Search di tabel (bagian 8b butir 1); perilaku FE tidak diasersi. TC-GS-DIV-262 mengasersi penolakan tanpa kode status karena TC tidak menyebut kodenya.
- Asersi absence (langkah 6, 13, 43, dan 56) didahului anchor positif pada tabel yang sama (langkah 4, 12, 42, dan 55; bagian 8b butir 2).
- Langkah penghubung: langkah 8, 15, dan 21 (membuka halaman Division sesudah ganti akun); langkah 3, 11, 18, 24, 31, 41, 54, dan 60 (Search nama yang diasersi atau menjadi target baris); langkah 5 (mengganti isi Search menjadi nama yang diasersi tidak ada); langkah 30, 44, 57, dan 71 (mengosongkan Search); langkah 38 sampai 40 dan 51 sampai 53 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`; verifikasi dialog pada langkah 39 dan 52 adalah asersi tambahan yang tidak ada di TC, ditulis agar penutupan form deterministik, konvensi bagian 10 S-08); langkah 59 (menunggu Create selesai); langkah 64 (membatalkan dialog `Delete Division`) dan langkah 70 (menutup Modal Changelog). Langkah 26 adalah aksi TC-GS-DIV-269. Penghapusan Division uji TC-GS-DIV-268 dilakukan oleh hook `after`.
- Langkah 13 (`Finance Bypass {runId}-073` tidak ada) menjadi bukti bahwa Edit langsung tidak mengubah Name (asersi tambahan). Expected Result b TC-GS-DIV-268 dipecah menjadi langkah 68 (skrip tidak dieksekusi) dan langkah 69 (tidak ada dialog browser). Langkah 27 (tidak ada toast error) tepat sesudah pemicu Search pada langkah 26.
- TC-GS-DIV-267 dan 270: Expected Result "penolakan server ditampilkan pada form" diasersi per klausa (langkah 48 sampai 50 dan 35 sampai 37); Division dipastikan tidak dibuat atau Name tidak berubah sesudah form ditutup (langkah 42 dan 56), karena tabel tertutup modal selama form terbuka.
- Spec melewati sekitar 35 langkah (71 langkah) karena memuat delapan TC kelas defense-in-depth dengan empat akun dan tiga kali ganti akun, dalam satu kelas harness. Rantai data: Division `Finance {runId}-073` dipakai bersama TC-GS-DIV-260, 261, dan 270 dan menjadi anchor positif asersi absence TC-GS-DIV-259 dan 267; sebagian besar langkah adalah Search, penutupan form dirty, serta verifikasi per klausa (S-01) yang tidak dapat digabung.
- Temuan untuk QA:
  - TC-GS-DIV-259, 260, 261, 262: TC tidak menyebut cara menangkap token sesi dan endpoint request langsung; keduanya disediakan tim FE dan dicatat di Prerequisites tanpa mengarang endpoint.
  - TC-GS-DIV-260: TC tidak memberi Name baru untuk request Edit `Finance`; spec memakai `Finance Bypass {runId}-073`.
  - TC-GS-DIV-262: TC tidak menyebut kelas respons penolakan guard in-use (PRD §9.3 hanya menyebut ditolak server); spec mengasersi penolakan tanpa kode status.
  - TC-GS-DIV-267 dan 270: TC tidak menyebut teks penolakan server pada form (PRD V-03 hanya mendefinisikan `Division Name contains invalid characters` untuk validasi klien); spec hanya mengasersi bahwa penolakan tampil pada form.
  - TC-GS-DIV-269: Post Condition `Data Division tidak berubah` tidak punya langkah observasi atau Expected padanan sehingga tidak diasersi.
  - TC-GS-DIV-268: Post Condition `Data Division tidak berubah` kontradiktif karena TC membuat Division `<script>alert(1)</script>`; Post Condition itu tidak diasersi. TC memakai Code `XSS1` literal yang bisa bentrok antar run bila cleanup gagal; spec membersihkannya di hook `before` dan `after`.
