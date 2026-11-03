---
id: TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af
title: "Validasi Edit Default User Not Yet Activated: Karakter, Email, Duplikat, dan Clear Field (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-530
  - TC-AC-ACC-531
  - TC-AC-ACC-527
  - TC-AC-ACC-528
  - TC-AC-ACC-532
  - TC-AC-ACC-533
  - TC-AC-ACC-521
  - TC-AC-ACC-522
coverage:
  web: automated
---

# Validasi Edit Default User Not Yet Activated: Karakter, Email, Duplikat, dan Clear Field (Active-Full)

## Prerequisites

- Mode: FE+BE. Semua `[Save]` diblokir; tidak ada data Client yang berubah.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (target Edit): Client `PT Teknologi Maju {runId}-068` (replika C-02: Active, Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari, Group Area Jakarta, FAMS Grace, Photo tersimpan, Client Code `TKM-{r6}`, Default User Not Yet Activated dengan Division seed `Finance` dan Position seed `Finance Manager`). Sumber duplikat (Pre-setup, hanya dibaca dan diketik): Email Default User A-16 `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net`. Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Nilai uji: emoji `😀` pada Company Name `PT 😀 Uji`, PIC Name `Rina 😀`, First Name `Budi 😀`, Last Name `Santoso 😀`; 121 karakter `a` pada First Name dan Last Name; Email 121 karakter = 109×`a` + `@example.com`.
- Kemampuan teknis: menempel dari clipboard, menginjeksi nilai langsung ke DOM lalu memicu event input.
- Cleanup: hook `after` menghapus Client seed lewat API.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Ketik Search `PT Teknologi Maju {runId}-068`, tekan Enter
2. Buka `⋯` baris `PT Teknologi Maju {runId}-068` lalu klik `Edit`

### TC-530: Format email salah

3. Ketik `company@` ke field Company Email lalu pindahkan fokus ke field lain
4. Verifikasi pesan error "Enter a valid email address" muncul pada Company Email setelah fokus berpindah
5. Ketik `user@` ke field Email Default User lalu pindahkan fokus ke field lain
6. Verifikasi pesan error "Enter a valid email address" muncul pada Email Default User setelah fokus berpindah
7. Kembalikan Company Email dan Email Default User ke nilai tersimpan

### TC-531: Nilai 121 karakter

8. Isi First Name dengan 121×`a`
9. Verifikasi pesan error "Max. 120 characters" pada First Name langsung saat nilai diisi
10. Isi Last Name dengan 121×`a`
11. Verifikasi pesan error "Max. 120 characters" pada Last Name langsung saat nilai diisi
12. Isi Email Default User dengan 109×`a` + `@example.com`
13. Verifikasi pesan error "Max. 120 characters" pada Email Default User langsung saat nilai diisi
14. Klik `[Save]`
15. Verifikasi popup tetap terbuka
16. Verifikasi tidak ada toast
17. Kembalikan First Name, Last Name, dan Email Default User ke nilai tersimpan

### TC-527: Emoji diblok saat ketik dan tempel

18. Untuk setiap field pada daftar Company Name, PIC Name, First Name, dan Last Name, lakukan langkah 19 sampai 21
19. Ketik nilai uji emoji ke field lalu kosongkan, kemudian tempel nilai uji emoji ke field
20. Verifikasi emoji tidak masuk ke field (diblok saat ketik dan saat tempel)
21. Verifikasi tidak ada pesan error pada field
22. Verifikasi popup tetap terbuka
23. Verifikasi tidak ada toast

### TC-528: Emoji yang lolos filter ditolak dengan pesan fallback

24. Injeksi `PT 😀 Uji` langsung ke DOM field Company Name lalu picu event input
25. Verifikasi pesan error inline Company Name: "Company name contains invalid characters" muncul langsung
26. Injeksi `Rina 😀` langsung ke DOM field PIC Name lalu picu event input
27. Verifikasi pesan error inline PIC Name: "PIC name contains invalid characters" muncul langsung
28. Injeksi `Budi 😀` langsung ke DOM field First Name lalu picu event input
29. Verifikasi pesan error inline First Name: "First name contains invalid characters" muncul langsung
30. Injeksi `Santoso 😀` langsung ke DOM field Last Name lalu picu event input
31. Verifikasi pesan error inline Last Name: "Last name contains invalid characters" muncul langsung
32. Verifikasi popup tetap terbuka
33. Verifikasi tidak ada toast
34. Kembalikan Company Name, PIC Name, First Name, dan Last Name ke nilai tersimpan

### TC-532 dan TC-533: Email Default User duplikat

35. Ketik Email Default User `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` tanpa memindahkan fokus
36. Verifikasi pesan error "Email already exists" muncul langsung (sekitar 500 ms setelah berhenti mengetik) tanpa menunggu fokus keluar dari field
37. Ganti isi Email Default User dengan email A-16 ditulis kapital seluruhnya dan diakhiri satu spasi (`CLIENTDEFAULTUSER_AUTOMATED_PTSEJAHTERAABADI@QWERTYSYSTEM.NET `), tanpa memindahkan fokus
38. Tunggu 1 detik
39. Verifikasi pesan error inline di bawah Email Default User: "Email already exists"
40. Kembalikan Email Default User ke nilai tersimpan

### TC-521: Clear Field mengosongkan seluruh field

41. Kosongkan Company Name
42. Klik `[Save]` hingga pesan error muncul
43. Verifikasi pesan error "Company name must not be empty" tampil
44. Klik `[Clear Field]`
45. Verifikasi Company Name, Client Code, Company Email, Website, Fax, PIC Name, PIC Email, PIC Phone, Address, Postal Code, First Name, Last Name, dan Email Default User kosong (bukan nilai semula)
46. Verifikasi Country menampilkan placeholder "Select country"
47. Verifikasi State menampilkan placeholder "Select state"
48. Verifikasi City menampilkan placeholder "Select city"
49. Verifikasi Industry menampilkan placeholder "Select industry"
50. Verifikasi Division menampilkan placeholder "Select division"
51. Verifikasi Position menampilkan placeholder "Select position"
52. Verifikasi pesan error "Company name must not be empty" hilang
53. Verifikasi popup Edit tetap terbuka
54. Verifikasi tidak ada dialog konfirmasi apa pun
55. Verifikasi kursor fokus berada di field input pertama form

### TC-522: Save setelah Clear Field

56. Klik `[Clear Field]`
57. Klik `[Save]`
58. Verifikasi Company Name: "Company name must not be empty"
59. Verifikasi Client Code: "Client code must not be empty" dan kolom tidak terisi otomatis
60. Verifikasi PIC Name: "PIC name must not be empty"
61. Verifikasi PIC Email: "PIC email must not be empty"
62. Verifikasi Address: "Address must not be empty"
63. Verifikasi Country: "Country must not be empty"
64. Verifikasi Postal Code: "Postal code must not be empty"
65. Verifikasi First Name: "First name must not be empty"
66. Verifikasi Last Name: "Last name must not be empty"
67. Verifikasi Email Default User: "Email must not be empty"
68. Verifikasi Division: "Division must not be empty"
69. Verifikasi popup tetap terbuka
70. Verifikasi tidak ada toast
71. Klik `[✕]` di header popup
72. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
73. Klik `[Leave]`
74. Klik Company Name `PT Teknologi Maju {runId}-068` untuk membuka Detail
75. Verifikasi Detail menampilkan Company Name "PT Teknologi Maju {runId}-068" dan Client Code "TKM-{r6}"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 90 langkah): satu popup Edit pada Client seed, satu role, satu kelas (validasi diblokir); Clear Field (TC-521, TC-522) ditaruh di akhir karena mengosongkan seluruh form; tiap blok berdiri sendiri dan form dipulihkan di antara blok. Langkah 19 sampai 21 diulang untuk 4 field.
- Langkah penghubung (S-03): pengembalian field ke nilai tersimpan; penutup `✕`, dialog `Unsaved Changes`, `[Leave]`; Detail membuktikan data tidak berubah (TC-522 butir m).
- Temuan untuk QA:
  - TC-521 butir e ("field input pertama form") tidak menyebut field mana; spec memakai redaksi TC.
  - TC-522 butir b: Client Code "tidak terisi otomatis" didahului `[Clear Field]` yang mengosongkan seluruh form; Division diasersi wajib walau Position opsional tidak diasersi.
