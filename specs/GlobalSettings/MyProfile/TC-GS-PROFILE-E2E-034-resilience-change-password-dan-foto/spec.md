---
id: TC-GS-PROFILE-E2E-034-resilience-change-password-dan-foto
title: "Resilience (Mock): Change Password, Edit Photo, dan Delete Photo Gagal 500, 403, dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-111
  - TC-GS-PROFILE-112
  - TC-GS-PROFILE-113
  - TC-GS-PROFILE-168
  - TC-GS-PROFILE-169
  - TC-GS-PROFILE-175
  - TC-GS-PROFILE-176
coverage:
  web: automated
---

# Resilience (Mock): Change Password, Edit Photo, dan Delete Photo Gagal 500, 403, dan Timeout

## Prerequisites

- Mode: mock (seluruh API di-mock; dijalankan tim FE sebagai integration test tanpa backend nyata).
- Aktor dimodelkan lewat payload identitas mock, tanpa login nyata: Pre-setup #7 (Maya Anggraini, Total Control, `Fixture.myProfile.accounts.password.email`; Time Format 24 jam, timezone Asia/Jakarta) untuk TC-GS-PROFILE-111, 112, dan 113; Pre-setup #9 (Nadia Putri, Total Control, `Fixture.myProfile.accounts.photo.email`; foto profil aktif `Fixture.myProfile.photo.nadiaActive`) untuk TC-GS-PROFILE-168, 169, 175, dan 176. Pergantian akun adalah pergantian payload identitas mock (Step ganti akun eksplisit).
- Nilai yang diketik pada form Change Password: Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD` (Pre-setup #7, nilai `Passw0rd!Old`), New Password dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3, nilai `N3wPassw0rd!`). Tidak ada login yang memakai password itu.
- File uji Edit Photo: `Fixture.myProfile.files.validPng` (`valid-photo.png`, Pre-setup #17), dipilih lewat kemampuan penanganan file picker native (disediakan tim FE).
- Halaman My Profile dibuka hook `beforeEach` suite dengan mock normal. Lihat `suite.md`, Hook suite 2.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook suite 1, 3, 4, 6, dan 7 mengelola backend nyata dan tidak berlaku pada spec mock ini (lihat Temuan untuk QA). Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` dijawab seen oleh mock (disediakan tim FE).
- Endpoint yang dipanggil halaman pada kondisi tes: berkas `openapi.yaml` dan `low-level-design.md` tidak ada di folder modul `global-settings/my-profile/` (keduanya diperiksa), sehingga path dan bentuk respons tidak dikarang dan seluruhnya disediakan tim FE:
  - Submit Change Password: respons 500 (TC-GS-PROFILE-111), 403 (TC-GS-PROFILE-112), dan tanpa respons / timeout klien (TC-GS-PROFILE-113).
  - Submit Edit Photo: respons 500 (TC-GS-PROFILE-168) dan timeout (TC-GS-PROFILE-169).
  - Submit Delete Photo: respons 500 (TC-GS-PROFILE-175) dan timeout (TC-GS-PROFILE-176).
  - Fetch My Profile dan Access & Status: normal sepanjang spec. Stream SSE bila halaman berlangganan: koneksi dijawab terbuka tanpa event.
- API pendukung di luar sumber modul disediakan tim FE: identitas pengguna, menu, dan flag Guided Tooltip.
- Jeda nyata 5 detik (pilihan spec, lebih panjang dari auto-hide toast sukses 4 detik menurut TL-11 TC) dipakai untuk membuktikan toast Error persisten.
- Tidak ada data backend atau state global yang diubah. Pemulihan: setiap mock dilepas segera sesudah blok TC-nya (S-09) dan sekali lagi di hook `after` walau spec gagal di tengah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-PROFILE-111: Change Password, respons 500 (Pre-setup #7)

1. Pasang mock respons 500 untuk submit Change Password
2. Klik [Change Password]
3. Isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
4. Klik [Save]
5. Verifikasi toast error "Error, failed to update your password."
6. Tunggu 5 detik
7. Verifikasi toast Error tidak hilang otomatis
8. Verifikasi modal Change Password tetap terbuka
9. Verifikasi Current Password, New Password, dan Confirm New Password tetap terisi
10. Verifikasi [Save] Enabled
11. Tutup (dismiss) toast Error

### TC-GS-PROFILE-112: Change Password, respons 403 (Pre-setup #7)

12. Ganti mock submit Change Password ke respons 403
13. Klik [Save]
14. Verifikasi toast error "You don't have permission to do this."
15. Verifikasi tidak ada redirect (pengguna tetap berada di My Profile)
16. Verifikasi modal Change Password tetap terbuka
17. Verifikasi ketiga field tetap terisi
18. Verifikasi [Save] Enabled
19. Tutup (dismiss) toast Error

### TC-GS-PROFILE-113: Change Password, timeout (Pre-setup #7)

20. Ganti mock submit Change Password ke tanpa respons (timeout)
21. Klik [Save]
22. Verifikasi toast error "Connection problem. Please try again."
23. Verifikasi toast tanpa tombol aksi
24. Verifikasi modal Change Password tetap terbuka
25. Verifikasi ketiga field tetap terisi
26. Verifikasi [Save] Enabled
27. Tutup (dismiss) toast Error
28. Klik [✕] pada modal Change Password
29. Verifikasi dialog "Unsaved Changes" tampil
30. Klik [Leave]
31. Lepas mock submit Change Password

### Ganti akun ke Pre-setup #9

32. Ganti akun: ubah identitas mock ke Pre-setup #9 (Nadia Putri) dengan semua mock normal, lalu muat ulang My Profile

### TC-GS-PROFILE-168: Edit Photo, respons 500 (Pre-setup #9)

33. Pasang mock respons 500 untuk submit Edit Photo
34. Hover Avatar lalu klik [Edit]
35. Pilih file `Fixture.myProfile.files.validPng`
36. Verifikasi toast error "Error, failed to update photo."
37. Tunggu 5 detik
38. Verifikasi toast Error tidak hilang otomatis
39. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
40. Tutup (dismiss) toast Error

### TC-GS-PROFILE-169: Edit Photo, timeout (Pre-setup #9)

41. Ganti mock submit Edit Photo ke tanpa respons (timeout)
42. Hover Avatar lalu klik [Edit]
43. Pilih file `Fixture.myProfile.files.validPng`
44. Verifikasi toast error "Connection problem. Please try again."
45. Verifikasi toast tanpa tombol aksi
46. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
47. Tutup (dismiss) toast Error
48. Lepas mock submit Edit Photo

### TC-GS-PROFILE-175: Delete Photo, respons 500 (Pre-setup #9)

49. Pasang mock respons 500 untuk submit Delete Photo
50. Hover Avatar lalu klik [Delete]
51. Klik [Remove]
52. Verifikasi toast error "Error, failed to remove photo."
53. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
54. Tutup (dismiss) toast Error

### TC-GS-PROFILE-176: Delete Photo, timeout (Pre-setup #9)

55. Ganti mock submit Delete Photo ke tanpa respons (timeout)
56. Hover Avatar lalu klik [Delete]
57. Klik [Remove]
58. Verifikasi toast error "Connection problem. Please try again."
59. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
60. Lepas mock submit Delete Photo

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-111, 112, 113, 168, 169, 175, 176). Tidak ada TC hanya-BE.
- Kelas harness b (fault injection / resilience), seluruhnya perilaku FE atas respons mock (konvensi bagian 6, Resilience `Mode: mock`). Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 dan 37 (jeda 5 detik untuk membuktikan toast Error persisten), langkah 11, 19, 27, 40, 47, dan 54 (dismiss toast Error sebelum toast Error berikutnya diasersi), langkah 12, 20, 33, 41, 49, dan 55 (mengganti atau memasang mock), langkah 28 sampai 31 (menutup modal terisi deterministik dan melepas mock), langkah 32 (Step ganti akun), langkah 48 dan 60 (melepas mock).
- TC-GS-PROFILE-112 dan 113 memakai form yang masih terisi dari TC-GS-PROFILE-111 (langkah 1 dan 2 TC dipenuhi oleh modal yang tetap terbuka dengan ketiga field terisi, diverifikasi di langkah 8 sampai 10); hanya mock dan klik [Save] yang diulang.
- Alasan spec melewati sekitar 35 langkah: seluruh blok berkelas b (resilience, `Mode: mock`) dengan mekanisme mock yang sama; tiap blok berdiri sendiri (mock dan aksi berbeda), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemisahan akan menambah hook dan pembukaan halaman tanpa pemisah nyata (prinsip 13: kelas ringan b satu spec per kelas per modul).
- Temuan untuk QA:
  - Hook suite 1 (login nyata), 3, 4, 6, dan 7 mengasumsikan backend nyata; spec `Mode: mock` memodelkan identitas lewat payload mock. Mekanisme hook suite untuk spec mock perlu dipastikan tim FE.
  - TC-GS-PROFILE-111 Post Condition "Password akun tidak berubah" (juga 112 dan 113) tanpa langkah observasi di TC dan tidak teramati pada mock tanpa backend; tidak diasersi (R-18).
  - TC-GS-PROFILE-168, 169, 175, dan 176 Post Condition "Foto aktif tetap `nadia-photo.jpg`" diasersi lewat Avatar (butir Expected); keadaan foto di server tidak diamati (butuh FE+BE).
  - TC tidak menyebut ambang timeout klien untuk TC-GS-PROFILE-113, 169, dan 176; ambang dan cara mock memutus respons ditetapkan tim FE.
  - TC-GS-PROFILE-175 dan 176 tidak menyatakan apakah dialog Remove Photo tertutup setelah toast Error; spec tidak menambah langkah penutupan dan langsung mengasersi Avatar.
