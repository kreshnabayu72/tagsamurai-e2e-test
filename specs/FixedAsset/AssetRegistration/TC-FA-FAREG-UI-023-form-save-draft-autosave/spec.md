---
id: TC-FA-FAREG-UI-023-form-save-draft-autosave
title: "Form Register Asset: Save draft, indikator autosave, Saving, dan respons gagal"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-01q", "S-REG-11", "S-REG-12", "S-REG-25", "T-REG-01", "T-REG-07", "T-REG-12", "T-REG-13", "T-REG-14", "V-REG-01", "§9.6#r1", "§9.6#r2", "§9.9#r5", "EB-ERR-1@save-draft", "EB-FB-1@save-draft", "EB-FB-3@edit-draft", "EB-FB-4", "EB-FRM-1@form-register-asset"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01q": [31, 35, 36, 37, 62, 63, 64, 66]
  "S-REG-11": [8, 10]
  "S-REG-12": [26, 28, 30]
  "S-REG-25": [35, 36, 39, 62, 63, 64, 66, 71, 76]
  "T-REG-01": [7, 48]
  "T-REG-07": 55
  "T-REG-12": 42
  "T-REG-13": 51
  "T-REG-14": 58
  "V-REG-01": 4
  "§9.6#r1": [7, 42, 43]
  "§9.6#r2": [28, 35, 36, 39]
  "§9.9#r5": [2, 4]
  "EB-ERR-1@save-draft": [42, 43, 44, 48, 51, 52]
  "EB-FB-1@save-draft": [7, 42]
  "EB-FB-3@edit-draft": 58
  "EB-FB-4": [13, 46]
  "EB-FRM-1@form-register-asset": [16, 17, 20, 22]
anchor: [12, 19]
coverage:
  web: automated
---

# Form Register Asset: Save draft, indikator autosave, Saving, dan respons gagal

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-023-1: Group `Gudang 1`, Assignable, bukan Excess.
  - DU-023-2: Item `Laptop Dell Latitude 5440` dengan Brand `Dell`, Model `Latitude 5440`, Quantity `3`.
  - DU-023-3: pilihan Group kosong, `Group` menampilkan `Select group`.
- Kondisi:
  - K1: form `Register Asset` baru; Group tidak dipilih (DU-023-3); tabel Item berisi DU-023-2.
  - K2: form `Register Asset` baru; Group DU-023-1 dipilih; tabel Item berisi DU-023-2; simpan draft berhasil.
  - K3: sama dengan K2; respons simpan draft lambat.
  - K4: form `Edit` draft tersimpan dengan Group DU-023-1 dan Item DU-023-2; autosave berjalan lambat lalu berhasil.
  - K5: sama dengan K4; autosave gagal pada siklus pertama dan berhasil pada siklus berikutnya.
  - K6: sama dengan K2; simpan draft gagal karena error server pada percobaan pertama dan berhasil pada percobaan kedua.
  - K7: sama dengan K2; simpan draft gagal karena gangguan jaringan.
  - K8: sama dengan K2; akses ubah draft aktor dicabut sesudah form dibuka sehingga simpan draft ditolak karena tanpa hak.
  - K9: form `Edit` draft tersimpan dengan Group DU-023-1 dan Item DU-023-2; tidak ada perubahan nilai sejak dibuka.
  - K10: sama dengan K4; Register Asset Bulk Limit bernilai `100`; autosave pada siklus pertama ditolak karena total aset melebihi Register Asset Bulk Limit; autosave pada siklus berikutnya diterima.

## Test Steps
### Save draft tanpa Group menampilkan pesan Group wajib
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi field `Group` belum berisi pilihan dan menampilkan `Select group` sebelum Save draft
3. Klik `[Save draft]`
4. Verifikasi pesan `Group must not be empty` tampil di bawah field `Group`

### Save draft berhasil menampilkan toast dan indikator Saved
5. Tampilkan Halaman `Register Asset` dengan kondisi K2
6. Klik `[Save draft]`
7. Verifikasi toast `Success, draft has been saved.` tampil
8. Verifikasi subjudul form pada tab `General Information` menampilkan `Saved`
9. Klik tab `Asset`
10. Verifikasi subjudul form pada tab `Asset` menampilkan `Saved`
11. Waktu berlalu sampai 5 detik sejak toast tampil
12. Verifikasi tombol `[Save draft]` masih tampil
13. Verifikasi toast `Success, draft has been saved.` tidak tampil lagi

### Save draft lambat membuat tombol dan kontrol form disabled
14. Tampilkan Halaman `Register Asset` dengan kondisi K3
15. Klik `[Save draft]`
16. Verifikasi tombol `[Save draft]` menampilkan loading dan Disabled
17. Verifikasi seluruh kontrol form dan tombol footer Disabled
18. Klik `[Save draft]` sekali lagi
19. Verifikasi tombol `[Save draft]` masih menampilkan loading
20. Verifikasi tidak ada pengiriman simpan draft kedua
21. Tunggu sampai respons simpan draft diterima
22. Verifikasi tombol `[Save draft]` kembali aktif

### Autosave menampilkan Saving lalu Saved tanpa toast
23. Tampilkan Halaman `Register Asset` dengan kondisi K4
24. Ganti isi sel `Quantity` Item pertama dengan `4`
25. Waktu berlalu sampai siklus autosave berjalan
26. Verifikasi subjudul form menampilkan `Saving...`
27. Tunggu sampai respons autosave diterima
28. Verifikasi subjudul form menampilkan `Saved`
29. Klik tab `Asset`
30. Verifikasi subjudul form pada tab `Asset` menampilkan `Saved`
31. Verifikasi tidak ada toast yang tampil sesudah autosave

### Autosave gagal menampilkan Not saved, mempertahankan data, dan dicoba lagi
32. Tampilkan Halaman `Register Asset` dengan kondisi K5
33. Ganti isi sel `Quantity` Item pertama dengan `4`
34. Waktu berlalu sampai siklus autosave pertama berjalan
35. Verifikasi subjudul form menampilkan `Not saved`
36. Verifikasi sel `Quantity` Item pertama masih menampilkan `4`
37. Verifikasi tidak ada toast yang tampil sesudah autosave gagal
38. Waktu berlalu sampai siklus autosave berikutnya selesai
39. Verifikasi subjudul form menampilkan `Saved`

### Save draft gagal karena error server
40. Tampilkan Halaman `Register Asset` dengan kondisi K6
41. Klik `[Save draft]`
42. Verifikasi toast Error `Error, failed to save draft.` tampil
43. Verifikasi form `Register Asset` tetap terbuka dan Item `Laptop Dell Latitude 5440` masih tampil
44. Verifikasi tombol `[Save draft]` aktif kembali
45. Waktu berlalu sampai 10 detik sejak toast tampil
46. Verifikasi toast `Error, failed to save draft.` masih tampil
47. Klik `[Save draft]`
48. Verifikasi toast `Success, draft has been saved.` tampil

### Save draft gagal karena gangguan jaringan
49. Tampilkan Halaman `Register Asset` dengan kondisi K7
50. Klik `[Save draft]`
51. Verifikasi toast Error `Connection problem. Please try again.` tampil
52. Verifikasi form `Register Asset` tetap terbuka dan Item `Laptop Dell Latitude 5440` masih tampil

### Save draft ditolak karena tanpa hak
53. Tampilkan Halaman `Register Asset` dengan kondisi K8
54. Klik `[Save draft]`
55. Verifikasi toast Error `You don't have permission to do this.` tampil

### Save draft tanpa perubahan menampilkan toast netral
56. Tampilkan Halaman `Register Asset` dengan kondisi K9
57. Klik `[Save draft]`
58. Verifikasi toast netral `No changes to save.` tampil

### Autosave diblokir pemeriksaan menampilkan Not saved, mempertahankan data, dan dicoba lagi
59. Tampilkan Halaman `Register Asset` dengan kondisi K10
60. Ganti isi sel `Quantity` Item pertama dengan `4`
61. Waktu berlalu sampai siklus autosave pertama berjalan
62. Verifikasi subjudul form menampilkan `Not saved`
63. Verifikasi sel `Quantity` Item pertama masih menampilkan `4`
64. Verifikasi tidak ada toast yang tampil sesudah autosave ditolak
65. Waktu berlalu sampai siklus autosave berikutnya selesai
66. Verifikasi subjudul form menampilkan `Saved`

### Autosave gagal menampilkan Not saved di subjudul tab Asset
67. Tampilkan Halaman `Register Asset` dengan kondisi K5
68. Ganti isi sel `Quantity` Item pertama dengan `4`
69. Waktu berlalu sampai siklus autosave pertama berjalan
70. Klik tab `Asset`
71. Verifikasi subjudul form pada tab `Asset` menampilkan `Not saved`

### Autosave diblokir pemeriksaan menampilkan Not saved di subjudul tab Asset
72. Tampilkan Halaman `Register Asset` dengan kondisi K10
73. Ganti isi sel `Quantity` Item pertama dengan `4`
74. Waktu berlalu sampai siklus autosave pertama berjalan
75. Klik tab `Asset`
76. Verifikasi subjudul form pada tab `Asset` menampilkan `Not saved`
