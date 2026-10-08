---
id: TC-GS-POS-E2E-025-race-bulk-delete
title: Race Bulk Delete saat status item berubah antara cek awal dan Confirm
priority: High
caseType: Edge Case
status: draft
sourceTc:
  - TC-GS-POS-81
coverage:
  web: automated
---

# Race Bulk Delete saat status item berubah antara cek awal dan Confirm

## Prerequisites

- Spec ini butuh dua sesi browser yang hidup bersamaan. Keduanya disiapkan tim FE di environment
  otomasi, dan keduanya login sebagai Role Total Control memakai kredensial yang sama dari
  `Spectra.env.ADMIN_USERNAME` dan `Spectra.env.ADMIN_PASSWORD`.
- Dua sesi dinotasikan sebagai `adminA` dan `adminB` supaya langkah bisa menyebut aktor dengan jelas.
- `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget` adalah Position bebas relasi yang ikut
  dipilih dalam batch, yaitu `Assistant Coordinator`. Posisi ini adalah item yang harus tetap terhapus
  normal.
- `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` adalah Position bebas relasi yang
  berubah status di tengah proses, yaitu `Data Entry Clerk`. Pada awal skenario posisinya belum
  direferensikan user.
- `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` adalah fixture FE yang meng-assign
  Position ke user bawaan, dipakai untuk membuat item Selected berubah status.
- `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference` adalah kebalikan dari fixture
  tersebut, dipakai untuk mengembalikan prasyarat setelah race selesai.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.title` adalah title Dialog 4, yaitu
  `Delete Positions`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.bodyQuestion` adalah kalimat penutup
  Dialog 4, yaitu `Are you sure you want to delete them? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete` adalah tombol
  konfirmasi Dialog 4, yaitu `Delete`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.title` adalah title Dialog 3, yaitu
  `Delete Positions`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillSkip` adalah heading kelompok
  yang dilewati, yaitu `The following are still in use and will be skipped:`
- `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue` adalah tombol
  konfirmasi Dialog 3, yaitu `Continue`.
- `Fixture.globalSettingsPosition.captions.modal.bulkDeletePartialSkipped` adalah toast untuk Delete yang
  sebagian berhasil, yaitu `Success, position has been deleted. Some items were skipped (still in use).`
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title` adalah title Dialog 1, yaitu
  `Delete Position`.
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.bodyQuestion` adalah kalimat penutup
  Dialog 1, yaitu `Are you sure you want to delete it? This action cannot be undone.`
- `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete` adalah tombol konfirmasi
  Dialog 1, yaitu `Delete`.
- `Fixture.globalSettingsPosition.captions.dialog.cannotDelete.title` adalah title Dialog 2, yaitu
  `Cannot Delete Data`.
- PRD §9.2 menetapkan dua fase cek untuk Bulk Delete. Cek awal menentukan dialog mana yang muncul dan
  boleh tidak atomik, sedangkan cek ulang atomik dijalankan bersama proses hapus di server per item.
  Kalau kondisi item berubah di antara cek awal dan Confirm, hasil final harus ikut kondisi terbaru dan
  item yang ternyata tidak aman di-skip ke ringkasan, bukan menggagalkan seluruh batch.
- Yang diuji di spec ini adalah re-cek atomik. Re-cek awal yang tidak atomik bukan bug, karena PRD
membolehkannya secara eksplisit.
- Konvensi platform menetapkan bahwa item yang di-skip dilaporkan lewat ringkasan pada toast atau
  dialog hasil, bukan dengan menggagalkan seluruh batch. Kalau satu item berubah status, item lain yang
  memang aman harus tetap terhapus.
- Jumlah entri log pada tiga surface dihitung di awal supaya item yang di-skip bisa dibedakan dari item
  yang benar-benar dihapus.
- Subbagian dipisah karena dua subbagian menghasilkan bentuk dialog hasil yang berbeda, yaitu
  Dialog 4 saat cek awal masih homogen dan Dialog 3 saat item sudah kelihatan terblokir.

## Test Steps

### Item berubah status setelah dialog konfirmasi tampil

1. Verifikasi tabel memuat `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget`
2. Verifikasi tabel memuat `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
3. Verifikasi kedua Position belum direferensikan user mana pun
4. Verifikasi tidak ada Bulk Action Bar yang tampil pada kondisi awal
5. Catat jumlah total Position
6. Catat jumlah entri log pada tiga surface sebelum subbagian ini
7. Di sesi `adminA`, centang checkbox pada baris
   `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget`
8. Di sesi `adminA`, centang checkbox pada baris
   `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
9. Verifikasi counter pada sesi `adminA` menunjukkan jumlah dua
10. Di sesi `adminA`, klik tombol aksi massa pada bar
11. Verifikasi dialog yang tampil pada sesi `adminA` adalah Dialog 4 dengan title
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.title`
12. Verifikasi dialog menampilkan bullet untuk kedua Position tanpa kelompok yang dilewati, karena pada
    saat cek awal keduanya memang aman
13. Verifikasi jumlah entri log belum berubah hanya karena membuka dialog
14. Di sesi `adminB`, jalankan `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
15. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` kini direferensikan user
16. Verifikasi dialog pada sesi `adminA` tidak berubah sendiri sebelum ada aksi dari user
17. Di sesi `adminA`, klik tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteHomogen.actions.delete`
18. Verifikasi proses tidak gagal secara total
19. Verifikasi toast
    `Fixture.globalSettingsPosition.captions.modal.bulkDeletePartialSkipped` muncul, karena ada satu
    item yang akhirnya tidak bisa diproses
20. Verifikasi toast itu menyebutkan ada item yang dilewati karena masih dipakai
21. Verifikasi dialog tertutup
22. Verifikasi baris
    `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget` tidak lagi ada di tabel
23. Verifikasi baris
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` tetap ada di tabel
24. Verifikasi jumlah total Position berkurang satu
25. Verifikasi Bulk Action Bar langsung hilang dan seleksi ter-reset ke nol
26. Verifikasi jumlah entri log Changelog bertambah satu entri untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget`
27. Verifikasi tidak ada entri log Delete untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
28. Verifikasi jumlah entri log Activity Log bertambah satu
29. Verifikasi jumlah entri System Log bertambah satu
30. Jalankan `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference` supaya prasyarat
    subbagian berikutnya tetap terpenuhi
31. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` kembali tidak
    direferensikan

### Item sudah terblokir saat cek awal sehingga dialog langsung Dialog 3

32. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` ada di tabel
33. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` tidak direferensikan user
34. Catat jumlah entri log pada tiga surface sebelum subbagian ini
35. Di sesi `adminB`, jalankan `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
36. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` kini direferensikan user
37. Di sesi `adminA`, buka ulang tabel dan centang checkbox pada baris
    `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget`
38. Di sesi `adminA`, centang checkbox pada baris
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
39. Verifikasi counter pada sesi `adminA` menunjukkan jumlah dua
40. Di sesi `adminA`, klik tombol aksi massa pada bar
41. Verifikasi dialog yang tampil adalah Dialog 3 dengan title
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.title`
42. Verifikasi dialog memuat kelompok
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.groupWillSkip`
43. Verifikasi kelompok tersebut memuat bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
44. Verifikasi dialog memuat kelompok yang akan dihapus dengan bullet untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget`
45. Verifikasi tombol konfirmasi berlabel
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue`, yaitu
    `Continue`, bukan `Delete`
46. Di sesi `adminB`, jalankan `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` untuk
    satu Position bebas relasi lain supaya ada perubahan kondisi tambahan tanpa menyentuh item yang
    sudah terblokir
47. Di sesi `adminA`, klik tombol
    `Fixture.globalSettingsPosition.captions.modal.bulkDeleteMixed.actions.continue`
48. Verifikasi proses tidak gagal secara total
49. Verifikasi toast
    `Fixture.globalSettingsPosition.captions.modal.bulkDeletePartialSkipped` muncul
50. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceSafeTarget` tidak lagi ada di tabel
51. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` tetap ada di tabel
52. Verifikasi jumlah entri log Changelog bertambah satu entri saja, yaitu untuk item yang benar-benar
    terhapus
53. Verifikasi jumlah entri log Activity Log bertambah satu
54. Verifikasi jumlah entri System Log bertambah satu
55. Jalankan `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference` untuk kedua Position
    yang dipakai pada subbagian ini
56. Verifikasi kedua Position tersebut kembali tidak direferensikan

### Re-cek awal boleh tidak atomik tapi hasilnya tidak boleh destructive

57. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` ada di tabel
58. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` tidak direferensikan user
59. Di sesi `adminA`, centang checkbox pada baris
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
60. Verifikasi counter pada sesi `adminA` menunjukkan jumlah satu
61. Di sesi `adminA`, buka dialog konfirmasi untuk Position tersebut
62. Verifikasi dialog yang tampil adalah Dialog 1 dengan title
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.title`, karena jumlah terpilih satu
    selalu collapse ke Dialog 1 maupun Dialog 2, bukan Dialog 4
63. Verifikasi dialog memakai kalimat penutup singular `delete it?`, yaitu
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.bodyQuestion`
64. Di sesi `adminB`, jalankan `Fixture.globalSettingsPosition.helpers.assignPositionToSeedUser` untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
65. Di sesi `adminA`, klik tombol
    `Fixture.globalSettingsPosition.captions.dialog.deleteConfirm.actions.delete`
66. Verifikasi hasil akhir adalah item yang dilewati, bukan item yang terhapus
67. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` tetap ada di tabel
68. Verifikasi tidak ada entri log Delete untuk
    `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget`
69. Jalankan `Fixture.globalSettingsPosition.helpers.releaseSeedUserReference`
70. Verifikasi `Fixture.globalSettingsPosition.bulkDelete.raceTurningTarget` kembali tidak
    direferensikan

## Notes

- Yang diuji di sini adalah re-cek atomik saat Confirm, bukan kecepatan request. PRD §9.2 membolehkan
  cek awal tidak atomik, jadi spec ini tidak menuntut apa pun dari fase cek awal selain menentukan dialog yang
  muncul.
- Subbagian pertama menguji kasus yang paling berbahaya, yaitu dialog sudah tampil sebagai homogen lalu
  satu item berubah status. Kalau implementasi memakai kondisi dari cek awal, Position yang sedang
  dipakai user akan terhapus dan data user rusak.
- Langkah 18 sampai 20 memeriksa bahwa kegagalan parsial dilaporkan, bukan dijadikan kegagalan total.
  Konvensi platform menetapkan item yang di-skip dilaporkan lewat ringkasan, dan kegagalan total akan
  membuat user menganggap tidak ada yang terhapus padahal ada.
- Langkah 22 sampai 24 adalah pembuktian bahwa item lain tetap terpengaruh. Kalau seluruh batch dibatalkan
  hanya karena satu item berubah, dan itu perilaku yang berbahaya, sehingga spec ini harus gagal di sana.
- Langkah 26 dan 27 memeriksa logging per item yang benar-benar terhapus, sama seperti di spec 024.
- Subbagian kedua menguji bentuk dialog hasil, yaitu Dialog 3 dengan kelompok yang dilewati. Bentuk ini
  berbeda dari subbagian pertama yang tetap memakai Dialog 4 dan baru melaporkannya lewat toast.
  Dua-duanya diizinkan karena yang tetap sama adalah isi akhir data.
- Subbagian ketiga sengaja hanya satu item terpilih supaya tidak ada batch yang bisa terhapus. Tujuannya
  murni membuktikan bahwa re-cek berlaku bahkan untuk batch kecil, karena ada implementasi yang hanya
  melakukan re-cek kalau jumlah item lebih dari satu.
- `adminB` selalu menyelesaikan aksinya lebih dulu secara eksplisit sebelum `adminA` menekan tombol
  konfirmasi, supaya urutan kejadiannya pasti dan tidak bergantung pada kecepatan klik.
- Semua subbagian mengembalikan relasi user di akhir, karena `Data Entry Clerk` dan Position lain yang
  dipakai di sini juga dipakai spec 017 dan spec 021. Kalau relasi itu tertinggal, spec-spec tersebut
  akan gagal karena alasan yang salah.
