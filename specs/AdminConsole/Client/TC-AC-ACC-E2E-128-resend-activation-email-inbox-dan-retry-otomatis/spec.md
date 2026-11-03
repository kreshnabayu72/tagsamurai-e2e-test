---
id: TC-AC-ACC-E2E-128-resend-activation-email-inbox-dan-retry-otomatis
title: "Resend Activation Email: Jumlah Email dan Log pada Dua Klik, Pembatalan Retry Otomatis, dan Pencatatan Send Activation Email"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-908
  - TC-AC-ACC-967
  - TC-AC-ACC-968
coverage:
  web: automated
---

# Resend Activation Email: Jumlah Email dan Log pada Dua Klik, Pembatalan Retry Otomatis, dan Pencatatan Send Activation Email

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun):
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-908). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD` (TC-AC-ACC-967 dan 968), lewat Step ganti akun eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup/A3: C-02 `PT Teknologi Maju` (Active, FAMS Grace, Default User Not Yet Activated; email awal `dewi.lestari@ptteknologimaju.test`; diubah ke `resend.uji@qwertysystem.net` lalu dipulihkan lewat Edit; efek: baris Changelog `Edit` dan `Resend Activation Email` serta Last Updated bertambah); C-FX9-1 `PT Resend Batal Retry` (Active, belum pernah memiliki subscription, Default User Not Yet Activated, email `resendbatalretry@qwertysystem.net`; Dikonsumsi) dan C-FX9-2 `PT Catat Kirim Berhasil` (Active, belum pernah memiliki subscription, Default User Not Yet Activated, email `catatkirimberhasil@qwertysystem.net`; Dikonsumsi). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-FX9-1 dan C-FX9-2 di hook `before` dan `after`.
- Kemampuan teknis (kelas harness eksternal; mail-catcher dan jam): mail-catcher/inbox yang dapat dibaca untuk `resend.uji@qwertysystem.net`, `resendbatalretry@qwertysystem.net`, dan `catatkirimberhasil@qwertysystem.net` dengan baseline jumlah email per alamat (R-11); memaksa email service gagal hanya pada percobaan kirim pertama (5xx) dan berhasil pada percobaan berikutnya (sisi server, disediakan tim FE/BE); mengaktifkan term pertama FAMS dari Admin Console > Client Subscription (alurnya dimiliki modul Client Subscription); mengatur jam server dan jam browser bersama (maju 30 menit pada TC-AC-ACC-967, maju 1 menit pada TC-AC-ACC-968) dan memulihkannya sebelum membaca Changelog dan notifikasi (S-09); membaca dropdown notifikasi navbar.
- Kemampuan teknis (sesi): sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser).
- Jeda percobaan ulang otomatis: 1 menit, 5 menit, dan 15 menit; antrean percobaan ulang dipicu dengan memajukan jam, lalu polling (muat ulang inbox tiap 5 detik, batas tunggu 2 menit).
- State global yang diubah dan dipulihkan di hook `after`: jam server dan jam browser, simulasi kegagalan email service. Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client dan Detail disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-908: Dua klik terpisah pada [Resend Activation Email] mengirim dua email dan menulis dua baris log

1. Ketik Search `PT Teknologi Maju`, tekan Enter
2. Klik `[⋯]` pada baris `PT Teknologi Maju` → klik `Edit`
3. Ubah Email Default User menjadi `resend.uji@qwertysystem.net`, lalu klik `[Save]`
4. Tunggu aksi selesai (form Edit tertutup)
5. Buka inbox `resend.uji@qwertysystem.net` dan catat jumlah email aktivasi (E0)
6. Klik ikon Changelog di toolbar List, ketik `Resend Activation Email` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris dengan Client Name `PT Teknologi Maju` (N0), lalu tutup modal
7. Ketik Search `PT Teknologi Maju`, tekan Enter, klik Company Name `PT Teknologi Maju`
8. Klik `[Resend Activation Email]`
9. Verifikasi toast sukses "Success, activation email has been sent."
10. Tunggu toast hilang
11. Klik `[Resend Activation Email]` lagi
12. Verifikasi toast sukses kedua "Success, activation email has been sent."
13. Klik breadcrumb "Client" untuk kembali ke List
14. Klik ikon Changelog di toolbar List, ketik `Resend Activation Email` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100
15. Verifikasi jumlah baris dengan Client Name `PT Teknologi Maju` adalah N0 + 2
16. Verifikasi dua baris baru ber-Action `Resend Activation Email` dan Field `Email`
17. Tutup modal Changelog, buka inbox `resend.uji@qwertysystem.net`, hitung email aktivasi (E1)
18. Verifikasi E1 adalah E0 + 2 (dua email aktivasi baru)
19. Pulihkan Email Default User `PT Teknologi Maju` ke `dewi.lestari@ptteknologimaju.test` lewat `[⋯]` → `Edit` → `[Save]`
20. Tunggu aksi selesai (form Edit tertutup)

### Blok Total Control

21. Ganti akun: logout lalu login sebagai Total Control A-01

#### TC-AC-ACC-967: Klik manual [Resend Activation Email] setelah percobaan pertama gagal membatalkan percobaan ulang otomatis yang tersisa

22. Buka dropdown notifikasi pada navbar, catat jumlah notifikasi berstatus Unread (N1), lalu tutup dropdown
23. Buka inbox `resendbatalretry@qwertysystem.net` dan catat jumlah Activation Email (E0)
24. Paksa email service gagal hanya pada percobaan kirim pertama (5xx) dan berhasil pada percobaan berikutnya
25. Aktifkan term pertama FAMS "PT Resend Batal Retry" dari Admin Console > Client Subscription
26. Verifikasi toast error "Error, failed to send activation email." ke aktor pemicu
27. Buka Admin Console > Client, klik sub-tab Active, ketik Search `PT Resend Batal Retry`, tekan Enter, klik Company Name `PT Resend Batal Retry`, dan lihat section Default User
28. Verifikasi section Default User menampilkan badge "Not Yet Activated"
29. Verifikasi `[Resend Activation Email]` tersedia
30. Klik `[Resend Activation Email]`
31. Verifikasi toast sukses "Success, activation email has been sent."
32. Buka inbox `resendbatalretry@qwertysystem.net` dan hitung Activation Email yang diterima (E1)
33. Verifikasi E1 adalah E0 + 1
34. Majukan jam server dan jam browser 30 menit (melampaui jeda percobaan ulang 1 menit, 5 menit, dan 15 menit), lalu polling antrean percobaan ulang (muat ulang inbox tiap 5 detik, batas tunggu 2 menit) dan hitung Activation Email di inbox (E2)
35. Verifikasi E2 adalah E1 (percobaan ulang otomatis yang tersisa dibatalkan oleh klik manual; tidak ada Activation Email tambahan)
36. Pulihkan jam server dan jam browser ke waktu nyata
37. Buka dropdown notifikasi pada navbar, catat jumlah Unread (N2), lalu tutup dropdown
38. Verifikasi N2 adalah N1 (tidak ada notifikasi "Activation email not delivered" baru)
39. Kembali ke Admin Console > Client, klik `[Changelog]` di toolbar List, ketik `PT Resend Batal Retry` di Search modal Changelog lalu tekan Enter, ubah ukuran halaman modal menjadi 100
40. Verifikasi tepat satu baris Action `Resend Activation Email` ber-Client Name "PT Resend Batal Retry"
41. Verifikasi baris itu ber-Field `Email`, Old Value `—`, New Value `resendbatalretry@qwertysystem.net`
42. Tutup modal Changelog

#### TC-AC-ACC-968: Changelog Send Activation Email ditulis satu baris per pengiriman yang berhasil, bukan per percobaan gagal

43. Klik `[Changelog]` di toolbar List, ketik `PT Catat Kirim Berhasil` di Search modal Changelog lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Send Activation Email` (N1), lalu tutup modal
44. Verifikasi N1 adalah 0
45. Buka inbox `catatkirimberhasil@qwertysystem.net` dan catat jumlah Activation Email (E0)
46. Paksa email service gagal hanya pada percobaan kirim pertama (5xx); percobaan ulang pertama (setelah 1 menit) berhasil
47. Aktifkan term pertama FAMS "PT Catat Kirim Berhasil" dari Admin Console > Client Subscription
48. Verifikasi toast error "Error, failed to send activation email." ke aktor pemicu
49. Buka Admin Console > Client, klik `[Changelog]` di toolbar List, ketik `PT Catat Kirim Berhasil` di Search modal Changelog lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Send Activation Email` (N2), lalu tutup modal
50. Verifikasi N2 adalah 0 (percobaan pertama yang gagal tidak menulis baris)
51. Majukan jam server dan jam browser 1 menit, lalu polling antrean percobaan ulang (muat ulang inbox tiap 5 detik, batas tunggu 2 menit) dan hitung Activation Email di inbox `catatkirimberhasil@qwertysystem.net` (E1)
52. Verifikasi E1 adalah E0 + 1
53. Pulihkan jam server dan jam browser ke waktu nyata
54. Klik `[Changelog]` di toolbar List, ketik `PT Catat Kirim Berhasil` di Search modal Changelog lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Send Activation Email` (N3)
55. Verifikasi N3 adalah 1
56. Verifikasi baris itu ber-Client Name "PT Catat Kirim Berhasil", Field `Email`, Old Value `—`, New Value `catatkirimberhasil@qwertysystem.net`, Modified By `System`
57. Verifikasi tidak ada baris Action `Resend Activation Email` baru untuk "PT Catat Kirim Berhasil"
58. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline inbox serta Changelog (S-12, R-11); ketiga TC satu harness eksternal (mail-catcher dengan pengaturan jam sebagai langkah rutin) dan tiap blok memakai Client sendiri atau memulihkan emailnya sehingga tetap bermakna walau blok sebelumnya gagal. Ganti akun sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras.
- Langkah penghubung (tanpa awalan Verifikasi): "Tunggu aksi selesai" sesudah Edit (langkah 4; langkah berikutnya berpindah surface), "Tunggu toast hilang" (langkah 10), ganti akun (langkah 21), pemulihan jam (langkah 36 dan 53, sebelum membaca notifikasi dan Changelog; S-09), pemulihan email Default User (langkah 19; Post Condition TC-AC-ACC-908), "Tunggu aksi selesai" sesudah pemulihan itu (langkah 20; langkah berikutnya mengganti akun) dan penutupan modal Changelog.
- Langkah 6 menyebut jumlah baris dengan Client Name `PT Teknologi Maju` termasuk baris seed L-08 dan baris dari langkah 3 (catatan TC-AC-ACC-908); baseline N0 dicatat sebelum aksi pemicu.
- Post Condition TC-AC-ACC-967 dan 968 (batalkan simulasi, pulihkan waktu, seed ulang) diwujudkan di hook `after` dan langkah 36 dan 53; TC-AC-ACC-968 butir a (N1 = 0) menjadi asersi pada langkah 44.
- Temuan untuk QA:
  - TC-AC-ACC-967 Expected d menyebut E1 = 1 dan e menyebut E2 = 1 sebagai nilai absolut; spec memakai selisih terhadap baseline inbox E0 (R-11, S-12).
  - TC-AC-ACC-967 langkah 3 dan TC-AC-ACC-968 langkah 3 ("Aktifkan term pertama FAMS dari Admin Console > Client Subscription") tidak merinci langkah di modul Client Subscription; spec menulis satu langkah dan tim FE menentukan alurnya.
  - TC-AC-ACC-968 Expected e menyebut "Modified By `System`" tanpa format `[First Name] [Last Initial]` karena aktor sistem; spec mengasersi persis `System`.
  - TC-AC-ACC-908 berlabel "Manual Only: inbox email asli" dan TC-AC-ACC-967/968 "memajukan waktu sistem": kebutuhan mail-catcher dan pengaturan jam dicatat di Prerequisites.
