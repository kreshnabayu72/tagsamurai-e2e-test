---
id: TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses
title: "Resend Activation Email: Hidden pada Client Tanpa Subscription Aktif, Archived, Activated, dan Sukses pada Active, Grace, Expired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-168
  - TC-AC-ACC-169
  - TC-AC-ACC-665
  - TC-AC-ACC-663
  - TC-AC-ACC-664
  - TC-AC-ACC-167
coverage:
  web: automated
---

# Resend Activation Email: Hidden pada Client Tanpa Subscription Aktif, Archived, Activated, dan Sukses pada Active, Grace, Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun):
  - Blok 1: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Blok 2 dan seterusnya: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`, lewat Step ganti akun eksplisit.
  - Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang hanya dibaca (tanpa aksi tulis): C-09 `PT Baru Daftar` (belum pernah memiliki subscription, Default User Not Yet Activated); C-AST-6 `PT Arsip Belum Aktif` (Archived, semua term Archive, Default User Not Yet Activated); C-01 `PT Sejahtera Abadi` (Default User Activated); C-07 `PT Cahaya Baru` (FAMS Waiting for Approval) dan C-08 `PT Mulai Esok` (FAMS Pending), keduanya Default User Not Yet Activated.
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): target `[Resend Activation Email]` bukan aksi baca: Resend menambah baris Changelog `Resend Activation Email` dan mengirim email, sehingga memakai replika `PT Teknologi Maju {runId}-120` (setara C-02: Active, FAMS Grace, SAMS dan SIEM No Subscription, Default User Not Yet Activated, Partner CV Mitra Sejati Anchor + CV Mitra Lestari, Group Area Jakarta), `PT Berakhir Belum Aktivasi {runId}-120` (setara C-LIF-5: Active, FAMS satu-satunya term Expired, SAMS dan SIEM tidak pernah berlangganan, Default User Not Yet Activated), dan `PT Aktif Plus Menunggu {runId}-120` (setara C-LIF-16: Active, FAMS Active, SAMS Waiting for Approval mode New, Default User Not Yet Activated). Email Default User ketiga replika bersuffix `{runId}-120` mengikuti S-12 (nilai disediakan Fixture BE; email awal fixture asal tidak tertulis lengkap di Tabel A3, lihat Temuan). Client C-02, C-LIF-5, dan C-LIF-16 literal tidak disentuh.
- Kemampuan teknis: pengiriman email aktivasi nyata; spec ini tidak membaca inbox (inbox asli hanya relevan untuk label "Manual Only" TC-AC-ACC-167 dan tidak ada dalam Expected).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Total Control

#### TC-AC-ACC-168: Resend Hidden bila belum ada subscription aktif atau Client Archived

1. Ketik Search `PT Baru Daftar`, tekan Enter
2. Klik Company Name `PT Baru Daftar` lalu lihat section Default User
3. Verifikasi section Default User menampilkan badge "Not Yet Activated"
4. Verifikasi `[Resend Activation Email]` Hidden
5. Klik breadcrumb "Client", klik sub-tab Archived, ketik Search `PT Arsip Belum Aktif`, tekan Enter
6. Klik Company Name `PT Arsip Belum Aktif` lalu lihat section Default User
7. Verifikasi section Default User menampilkan badge "Not Yet Activated"
8. Verifikasi `[Resend Activation Email]` Hidden

### Blok 2: Active-Full

9. Ganti akun: logout lalu login sebagai Active-Full A-15

#### TC-AC-ACC-169: Resend Hidden bila Default User sudah Activated

10. Ketik Search `PT Sejahtera Abadi`, tekan Enter
11. Klik Company Name `PT Sejahtera Abadi`
12. Verifikasi `[Resend Activation Email]` Hidden
13. Verifikasi status Default User "Activated"

#### TC-AC-ACC-665: Resend Hidden pada Client Not Yet Activated dengan term hanya Waiting for Approval atau Pending

14. Klik breadcrumb "Client", ketik Search `PT Cahaya Baru`, tekan Enter
15. Klik Company Name `PT Cahaya Baru` lalu lihat section Default User
16. Verifikasi section Default User menampilkan badge "Not Yet Activated"
17. Verifikasi `[Resend Activation Email]` Hidden
18. Klik breadcrumb "Client", ketik Search `PT Mulai Esok`, tekan Enter
19. Klik Company Name `PT Mulai Esok` lalu lihat section Default User
20. Verifikasi section Default User menampilkan badge "Not Yet Activated"
21. Verifikasi `[Resend Activation Email]` Hidden

#### TC-AC-ACC-663: Resend tampil dan terkirim untuk Client Not Yet Activated dengan FAMS Grace

22. Klik breadcrumb "Client", klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Teknologi Maju {runId}-120` lalu tekan Enter
23. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Resend Activation Email` untuk "PT Teknologi Maju {runId}-120" (N0), lalu tutup modal
24. Ketik Search `PT Teknologi Maju {runId}-120`, tekan Enter
25. Klik Company Name `PT Teknologi Maju {runId}-120` lalu lihat section Default User
26. Verifikasi section Default User menampilkan badge "Not Yet Activated"
27. Verifikasi section Default User menampilkan tombol `[Resend Activation Email]`
28. Klik `[Resend Activation Email]`
29. Verifikasi toast sukses "Success, activation email has been sent."
30. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)
31. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Teknologi Maju {runId}-120` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
32. Verifikasi jumlah baris Action `Resend Activation Email` untuk "PT Teknologi Maju {runId}-120" adalah N0 + 1
33. Verifikasi baris baru: Action `Resend Activation Email`, Client Name "PT Teknologi Maju {runId}-120", Field `Email`, Old Value `—`, New Value email Default User "PT Teknologi Maju {runId}-120"
34. Tutup modal Changelog

#### TC-AC-ACC-664: Resend tampil dan terkirim untuk Client Not Yet Activated dengan FAMS Expired

35. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-120` lalu tekan Enter
36. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Resend Activation Email` untuk "PT Berakhir Belum Aktivasi {runId}-120" (N0), lalu tutup modal
37. Ketik Search `PT Berakhir Belum Aktivasi {runId}-120`, tekan Enter
38. Klik Company Name `PT Berakhir Belum Aktivasi {runId}-120` lalu lihat section Default User
39. Verifikasi section Default User menampilkan badge "Not Yet Activated"
40. Verifikasi section Default User menampilkan tombol `[Resend Activation Email]`
41. Klik `[Resend Activation Email]`
42. Verifikasi toast sukses "Success, activation email has been sent."
43. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)
44. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Berakhir Belum Aktivasi {runId}-120` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
45. Verifikasi jumlah baris Action `Resend Activation Email` untuk "PT Berakhir Belum Aktivasi {runId}-120" adalah N0 + 1
46. Verifikasi baris baru: Action `Resend Activation Email`, Client Name "PT Berakhir Belum Aktivasi {runId}-120", Field `Email`, Old Value `—`, New Value email Default User "PT Berakhir Belum Aktivasi {runId}-120"
47. Tutup modal Changelog

#### TC-AC-ACC-167: Resend Activation Email saat Not Yet Activated dan sudah ada subscription aktif

48. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Aktif Plus Menunggu {runId}-120` lalu tekan Enter
49. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Resend Activation Email` untuk "PT Aktif Plus Menunggu {runId}-120" (N0), lalu tutup modal
50. Ketik Search `PT Aktif Plus Menunggu {runId}-120`, tekan Enter
51. Klik Company Name `PT Aktif Plus Menunggu {runId}-120`
52. Klik `[Resend Activation Email]`
53. Verifikasi toast sukses "Success, activation email has been sent."
54. Tunggu aksi selesai (tombol `[Resend Activation Email]` aktif kembali)
55. Klik breadcrumb "Client" lalu klik `[Changelog]` di toolbar, klik ikon Search di modal Changelog, ketik `PT Aktif Plus Menunggu {runId}-120` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
56. Verifikasi jumlah baris Action `Resend Activation Email` untuk "PT Aktif Plus Menunggu {runId}-120" adalah N0 + 1
57. Verifikasi baris baru: Action `Resend Activation Email`, Client Name "PT Aktif Plus Menunggu {runId}-120", Field `Email`, Old Value `—`, New Value email Default User "PT Aktif Plus Menunggu {runId}-120"
58. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan empat blok Resend yang berulang dengan pola sama (baseline Changelog, Resend, baca Changelog); semua blok satu topik (Resend Activation Email), satu kelas harness, dan tiap blok memakai Client sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Ganti akun lewat Step eksplisit (Total Control ke Active-Full) sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 9 (ganti akun), penutupan modal Changelog, "Tunggu aksi selesai" sesudah Resend karena langkah berikutnya berpindah surface (butir 8 bagian 8b), dan Search yang menemukan baris target (R-16). Langkah baseline Changelog (22-23, 35-36, 48-49) mengikuti S-12 (selisih jumlah, bukan posisi teratas); TC hanya menyebut "memuat baris Action `Resend Activation Email`".
- Screening Hidden (TC-AC-ACC-168, 169, 665) mendahului aksi Resend sukses dalam spec (prinsip 2); Hidden pada Client Archived memakai sub-tab Archived.
- Post Condition semua TC di spec ini: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-663, 664, 167 Expected c menyebut "New Value email Default User <nama Client>" tanpa menyebut nilai email; email `PT Teknologi Maju` hanya tertulis di TC-AC-ACC-908 (`dewi.lestari@ptteknologimaju.test`, email C-02 yang tidak menerima surel), sedangkan email `PT Berakhir Belum Aktivasi` dan `PT Aktif Plus Menunggu` tidak tertulis di Tabel A3; spec mengasersi "email Default User" replika dan nilainya dibaca dari seed Fixture BE (disediakan tim FE).
  - TC-AC-ACC-167 berlabel "Manual Only: inbox email asli" tetapi Expected tidak memuat asersi inbox; spec tidak membaca inbox.
  - TC-AC-ACC-168 Expected a dan b tidak menyebut Resend Hidden pada kombinasi Client Archived dengan subscription aktif; hanya dua Client yang disebut TC yang diuji.
