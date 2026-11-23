---
id: TC-FA-FAAC-E2E-212-helper-equivalent-declining-rate-pembulatan-dan-fallback
title: "Create Asset Class: Helper Equivalent di Bawah Declining Rate, Kelipatan Tarif Garis Lurus, Pembulatan Half-Up, dan Kembali ke Helper Bawaan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-728
  - TC-FA-FAAC-729
  - TC-FA-FAAC-735
  - TC-FA-FAAC-730
sourceRules: ["FAAC-LOGIC-02j", "FAAC-LOGIC-02b", "ST-35", "FI-17", "FLD-08", "V-11", "V-13"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-02j": [4, 6, 9, 13, 15, 21, 23, 25, 34]
  "FAAC-LOGIC-02b": [31, 38]
  "ST-35": [4, 6, 9, 13, 21, 25, 34, 40]
  "FI-17": [6, 9, 13, 15, 21, 23, 34]
  "FLD-08": [6, 9, 13, 21]
  "V-11": 38
  "V-13": 31
coverage:
  web: automated
---

# Create Asset Class: Helper Equivalent di Bawah Declining Rate, Kelipatan Tarif Garis Lurus, Pembulatan Half-Up, dan Kembali ke Helper Bawaan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: tidak ada yang dipakai selain akun aktor. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec hanya mengetik Useful Life dan Declining Rate di form Create tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: tidak ada selain browser; langkah 14 mengetik langsung di input Declining Rate dan membaca helper tanpa blur, Tab, Enter, atau Save.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`
3. Pilih Method `Declining Balance`

### TC-FA-FAAC-728: Helper di bawah Declining Rate: helper bawaan digantikan helper Equivalent yang menampilkan kelipatan tarif garis lurus

4. Verifikasi di bawah input Declining Rate tampil helper bawaan `Use the rate set by your company's accounting policy.` sebelum Useful Life dan Declining Rate diisi
5. Verifikasi helper `Equivalent to [Factor]× the straight-line rate` tidak tampil sebelum Useful Life dan Declining Rate diisi
6. Isi Useful Life `48` dan Declining Rate `50`
7. Verifikasi helper bawaan digantikan helper `Equivalent to 2.0× the straight-line rate`
8. Ubah Useful Life menjadi `120` dan Declining Rate menjadi `90`
9. Verifikasi helper berubah menjadi `Equivalent to 9.0× the straight-line rate`
10. Verifikasi input Useful Life dan Declining Rate tetap dapat diedit
11. Verifikasi tidak ada caption error

### TC-FA-FAAC-729: Helper Equivalent dibulatkan half-up ke 1 desimal dan dihitung ulang seketika

12. Isi Useful Life `60` dan Declining Rate `33`
13. Verifikasi helper `Equivalent to 1.7× the straight-line rate` (1.65 dibulatkan ke atas)
14. Ubah Declining Rate menjadi `21` dengan mengetik langsung tanpa menekan Tab atau Enter, tanpa klik di luar field, dan tanpa Save
15. Verifikasi helper `Equivalent to 1.1× the straight-line rate` (1.05 dibulatkan ke atas), sudah berubah segera setelah digit terakhir diketik saat fokus masih di input Declining Rate
16. Ubah Useful Life menjadi `48` dan Declining Rate menjadi `25.5`
17. Verifikasi helper `Equivalent to 1.0× the straight-line rate` (1.02 ditulis dengan satu desimal)
18. Ubah Useful Life menjadi `36` dan Declining Rate menjadi `50`
19. Verifikasi helper `Equivalent to 1.5× the straight-line rate`

### TC-FA-FAAC-735: Helper Equivalent memakai 1200 ÷ Useful Life tanpa pembulatan sebelum pembagian

20. Isi Useful Life `84` dan Declining Rate `25`
21. Verifikasi helper `Equivalent to 1.8× the straight-line rate` (25 ÷ (1200 ÷ 84) = 1.75 dibulatkan half-up ke 1.8, bukan 1.7)
22. Ubah Declining Rate menjadi `75`
23. Verifikasi helper `Equivalent to 5.3× the straight-line rate` (75 ÷ (1200 ÷ 84) = 5.25 dibulatkan half-up ke 5.3, bukan 5.2)

### TC-FA-FAAC-730: Helper di bawah Declining Rate kembali ke helper bawaan bila Useful Life atau Declining Rate kosong atau tidak valid dan tidak memblokir input

24. Kosongkan Useful Life dan isi Declining Rate `50`
25. Verifikasi helper `Equivalent to [Factor]× the straight-line rate` tidak tampil
26. Verifikasi di bawah input Declining Rate tampil helper bawaan `Use the rate set by your company's accounting policy.`
27. Isi Useful Life `48` lalu kosongkan Declining Rate
28. Verifikasi helper `Equivalent to [Factor]× the straight-line rate` tidak tampil
29. Verifikasi di bawah input Declining Rate tampil helper bawaan `Use the rate set by your company's accounting policy.`
30. Isi Declining Rate `101`
31. Verifikasi caption `Declining rate must be between 0 and 100` menggantikan helper di bawah input Declining Rate
32. Verifikasi helper Equivalent dan helper bawaan tidak tampil
33. Ubah Declining Rate menjadi `90` dan Useful Life menjadi `120`
34. Verifikasi helper `Equivalent to 9.0× the straight-line rate` tampil
35. Verifikasi Declining Rate `90` diterima tanpa caption
36. Verifikasi input Declining Rate tidak terkunci
37. Ubah Useful Life menjadi `601`
38. Verifikasi caption `Useful life must be between 1 and 600 months` tampil di bawah Useful Life
39. Verifikasi helper Equivalent tidak tampil
40. Verifikasi di bawah input Declining Rate kembali tampil helper bawaan `Use the rate set by your company's accounting policy.`
41. Ganti Method menjadi `Straight Line`
42. Verifikasi field Declining Rate beserta helper-nya tidak tampil
43. Klik breadcrumb `Asset Class`
44. Verifikasi dialog `Unsaved Changes` tampil
45. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-728, 729, 735, 730). Tidak ada TC hanya-BE di spec ini; keempatnya bertanda UI Only dan spec tetap `Mode: FE+BE` karena dijalankan di suite FE+BE.
- Urutan blok: TC-735 diletakkan sebelum TC-730 (perubahan urutan terhadap nomor TC, S-10), karena TC-730 mengakhiri dengan nilai tidak valid dan pergantian Method sehingga menjadi blok terakhir; keempat blok memakai satu pembukaan form (prinsip 6 dan 8, halaman yang sama dipakai berulang untuk kasus yang hanya mengetik tanpa submit). Langkah 1 sampai 3 identik di keempat TC. Langkah TC-730 nomor 2 ("pilih Declining Balance dan perhatikan area di bawah input Declining Rate") diasersi pada langkah 4 dan 5 tepat sesudah Method dipilih, sebelum Useful Life dan Declining Rate diisi.
- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 43 sampai 45 menutup form dirty lewat breadcrumb (S-08; `Verifikasi` dialog `Unsaved Changes` diwajibkan S-08).
- Langkah 15 diasersi segera setelah digit terakhir diketik sebelum langkah yang mengubah state fokus (bagian 8b butir 5).
- Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah; keempat blok TC satu topik (helper Equivalent di bawah Declining Rate), satu layar, tanpa data dibuat dan tanpa cleanup; satu pembukaan form dipakai bersama sesuai bagian 3 ("Halaman yang sama dipakai berulang"), dan jumlah langkah didorong oleh `Verifikasi` per klausa (S-01).
- Asersi absence langkah 5, 25, 28, 32, 39, dan 42 punya anchor positif pada surface yang sama (helper bawaan, caption, atau field lain pada kartu Commercial yang sudah termuat; bagian 8b butir 2).
- Temuan untuk QA: (a) TC-728 butir d ("tidak ada caption error") dan TC-730 butir c ("input tidak terkunci") tidak menyebut cara membuktikan input tidak terkunci selain input tetap dapat diedit; spec mengasersi caption tidak ada dan input tidak terkunci tanpa menambah langkah mengetik. (b) TC-730 butir a menyebut `[Factor]` sebagai pola helper tanpa angka; spec menulisnya apa adanya. (c) Nilai `Declining Rate 101` pada TC-730 langkah 5 memicu caption V-13; Useful Life `601` memicu caption V-11.
