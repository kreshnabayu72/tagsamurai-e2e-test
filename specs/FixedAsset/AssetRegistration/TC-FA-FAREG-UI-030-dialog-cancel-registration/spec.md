---
id: TC-FA-FAREG-UI-030-dialog-cancel-registration
title: "Dialog Cancel Registration: isi, checkbox, dialog blok, dan toast"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-REG-14, D-REG-17, T-REG-10, T-REG-12, T-REG-13, §9.6#r5, §9.9#r18, EB-ERR-1@cancel-registration, EB-FB-1@cancel-registration]
smoke: []
dependsOn: []
trace:
  D-REG-14: [2, 3, 4, 5, 6, 8, 9, 10, 11, 14, 15, 16, 18, 21]
  D-REG-17: [48, 49, 50, 52, 55, 56, 57]
  T-REG-10: 24
  T-REG-12: [29, 34]
  T-REG-13: 43
  §9.6#r5: [24, 25, 29]
  §9.9#r18: [6, 7]
  EB-ERR-1@cancel-registration: [30, 31, 32, 40, 44, 45]
  EB-FB-1@cancel-registration: [24, 29, 37, 39]
anchor: []
coverage:
  web: automated
---

# Dialog Cancel Registration: isi, checkbox, dialog blok, dan toast

## Prerequisites
- Aktor: Hadi K (pengaju pengajuan, role Manage asset & TAG, cakupan Group terkelola).
- Layar awal: halaman Detail pengajuan Waiting for Approval milik Hadi K, tempat dialog `Cancel Registration` terbuka dari `[Cancel Registration]` pada footer.
- Komponen: Dialog `Cancel Registration` (`D-REG-14`)
- Data:
  - DU-030-1: pengajuan Registration ID `REG-20261108-00011`, Status `Waiting for Approval`, Group `Kantor Pusat`, Total Asset `4`, dengan keterangan aset yang bila ditampilkan berbentuk `4 assets`.
  - DU-030-2: pengguna Name `Agus P` (approver lain, role Total Control, cakupan seluruh client).
  - Teks dialog `Cannot Cancel` yang diharapkan `This request was already decided by Agus P.`, dari template `This request was already decided by [User].` dan User `Agus P`.
- Kondisi:
  - K1: dialog dibuka untuk pengajuan DU-030-1.
  - K2: dialog dibuka untuk pengajuan DU-030-1, dan menyimpan pembatalan gagal karena error server.
  - K3: dialog dibuka untuk pengajuan DU-030-1, dan menyimpan pembatalan berhasil.
  - K4: dialog dibuka untuk pengajuan DU-030-1, menyimpan pembatalan gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan kedua.
  - K5: dialog dibuka untuk pengajuan DU-030-1, dan menyimpan pembatalan gagal karena koneksi terputus.
  - K6: dialog dibuka untuk pengajuan DU-030-1, dan jawaban server menyatakan pengajuan sudah diputuskan oleh pengguna DU-030-2.
  - K7: dialog dibuka untuk pengajuan DU-030-1, dan jawaban server menyatakan pengajuan tidak lagi Waiting for Approval.

## Test Steps

### Isi dialog Cancel Registration
1. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K1
2. Verifikasi judul dialog `Cancel Registration`
3. Verifikasi bullet pada body dialog memuat Registration ID pengajuan
4. Verifikasi dialog tidak menampilkan Group `Kantor Pusat`
5. Verifikasi dialog tidak menampilkan keterangan jumlah aset `4 assets`
6. Verifikasi body dialog memuat checkbox `Save as Draft to edit`
7. Verifikasi checkbox `Save as Draft to edit` tercentang
8. Verifikasi teks bantu `The assets return to Draft and their reserved quota is released.` tampil
9. Verifikasi pertanyaan konfirmasi `Are you sure you want to cancel it?`
10. Verifikasi footer dialog memuat tombol `[Go Back]`
11. Verifikasi footer dialog memuat tombol `[Cancel Registration]`

### Teks bantu mengikuti checkbox
12. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K1
13. Klik checkbox `Save as Draft to edit`
14. Verifikasi checkbox `Save as Draft to edit` tidak tercentang
15. Verifikasi teks bantu `The assets will be discarded and their reserved quota is released. This can't be undone.` tampil
16. Verifikasi teks bantu `The assets return to Draft and their reserved quota is released.` tidak tampil
17. Klik checkbox `Save as Draft to edit`
18. Verifikasi teks bantu `The assets return to Draft and their reserved quota is released.` tampil

### Go Back menutup dialog
19. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K1
20. Klik tombol `[Go Back]`
21. Verifikasi dialog `Cancel Registration` tertutup

### Pembatalan berhasil
22. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K3
23. Klik tombol `[Cancel Registration]` pada footer dialog
24. Verifikasi toast sukses `Success, registration has been canceled.`
25. Verifikasi dialog `Cancel Registration` tertutup

### Pembatalan gagal karena error server
26. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K2
27. Klik checkbox `Save as Draft to edit`
28. Klik tombol `[Cancel Registration]` pada footer dialog
29. Verifikasi toast error `Error, failed to cancel registration.`
30. Verifikasi dialog `Cancel Registration` tetap terbuka
31. Verifikasi checkbox `Save as Draft to edit` tetap tidak tercentang
32. Verifikasi tombol `[Cancel Registration]` pada footer dialog aktif lagi
33. Waktu berlalu sampai 10 detik sejak toast error tampil
34. Verifikasi toast error `Error, failed to cancel registration.` masih tampil

### Kirim ulang sesudah pulih berhasil sekali
35. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K4
36. Klik tombol `[Cancel Registration]` pada footer dialog
37. Verifikasi toast error `Error, failed to cancel registration.`
38. Klik tombol `[Cancel Registration]` pada footer dialog
39. Verifikasi toast sukses `Success, registration has been canceled.`
40. Verifikasi hanya satu toast sukses yang tampil

### Pembatalan gagal karena koneksi terputus
41. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K5
42. Klik tombol `[Cancel Registration]` pada footer dialog
43. Verifikasi toast error `Connection problem. Please try again.`
44. Verifikasi dialog `Cancel Registration` tetap terbuka
45. Verifikasi tombol `[Cancel Registration]` pada footer dialog aktif lagi

### Pengajuan sudah diputuskan pengguna lain
46. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K6
47. Klik tombol `[Cancel Registration]` pada footer dialog
48. Verifikasi dialog `Cannot Cancel` tampil
49. Verifikasi isi dialog `This request was already decided by Agus P.`
50. Verifikasi dialog `Cannot Cancel` memuat tombol `[OK]`
51. Klik tombol `[OK]`
52. Verifikasi dialog `Cannot Cancel` tertutup

### Pengajuan tidak lagi Waiting for Approval
53. Tampilkan Dialog `Cancel Registration` (`D-REG-14`) dengan kondisi K7
54. Klik tombol `[Cancel Registration]` pada footer dialog
55. Verifikasi dialog `Cannot Cancel` tampil
56. Verifikasi isi dialog `This request is no longer waiting for approval.`
57. Verifikasi dialog `Cannot Cancel` memuat tombol `[OK]`
