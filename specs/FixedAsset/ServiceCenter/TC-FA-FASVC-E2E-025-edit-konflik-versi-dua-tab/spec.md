---
id: TC-FA-FASVC-E2E-025-edit-konflik-versi-dua-tab
title: "Edit dengan Versi Usang: Dialog Service Center Changed, Form Diisi Ulang"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FASVC-LOGIC-11c, EC-FASVC-03b, DO-FASVC-07, F-FASVC-02.k4]
smoke: []
dependsOn: []
trace:
  FASVC-LOGIC-11c: [8, 28]
  EC-FASVC-03b: 7
  DO-FASVC-07: [9, 11, 12, 28, 29, 32, 33]
  F-FASVC-02.k4: [17, 22]
anchor: [3, 15, 20]
coverage:
  web: automated
---

# Edit dengan Versi Usang: Dialog Service Center Changed, Form Diisi Ulang

## Prerequisites
- Aktor: Total Control. Admin A (`Rina Wulandari {runId}`, role Total Control, cakupan seluruh Group) menguji layarnya. Admin B (`Budi Santoso {runId}`, role Total Control, cakupan seluruh Group) memicu perubahan dari konteks lain.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-025-1: Service Center `Bengkel Mitra Teknik {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company phone `+62 81234500125`, Company email `servis@mitrateknik.example`, Status `Active`, ada di entitas aktor.
  - DU-025-2: Name hasil Edit Admin B `Bengkel Mitra Teknik Utama {runId}`.
  - DU-025-3: Name yang dicoba disimpan Admin A `Bengkel Mitra Teknik Servis {runId}`.
  - DU-025-4: Service Center `Bengkel Rekanan Prima {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Malang`, Company phone `+62 81234500126`, Company email `servis@rekananprima.example`, Status `Active`, ada di entitas aktor.
  - DU-025-5: Name hasil Edit Admin B `Bengkel Rekanan Prima Utama {runId}`.

## Test Steps

### Edit dengan versi usang ditolak dengan dialog Service Center Changed
1. Ketik Search `Bengkel Mitra Teknik {runId}`, tekan Enter
2. Klik `⋯` pada baris `Bengkel Mitra Teknik {runId}`, lalu klik `Edit`
3. Verifikasi dialog `Edit Service Center` terbuka dengan field Name berisi `Bengkel Mitra Teknik {runId}`
4. Admin B mengubah Name `Bengkel Mitra Teknik {runId}` menjadi `Bengkel Mitra Teknik Utama {runId}` lewat Edit dan menyimpannya
5. Ganti isi field Name pada dialog `Edit Service Center` dengan `Bengkel Mitra Teknik Servis {runId}`
6. Klik `[Save]`
7. Verifikasi dialog `Service Center Changed` tampil pada simpan kedua Admin A
8. Verifikasi dialog memuat pesan `This service center was changed by someone else. Please review.`
9. Verifikasi dialog `Service Center Changed` memiliki tombol `[OK]`

### Form Edit diisi ulang dengan data terbaru dan tetap terbuka
10. Klik `[OK]`
11. Verifikasi dialog `Edit Service Center` tetap terbuka
12. Verifikasi field Name berisi `Bengkel Mitra Teknik Utama {runId}`, nilai terbaru dari Admin B

### Nilai Admin A ditolak: tidak tersimpan dan tidak tercatat
13. Klik `✕` pada form yang belum diubah sejak diisi ulang
14. Ganti isi kotak Search dengan `Bengkel Mitra Teknik Utama {runId}`, tekan Enter
15. Verifikasi baris `Bengkel Mitra Teknik Utama {runId}` tampil di tabel
16. Ganti isi kotak Search dengan `Bengkel Mitra Teknik Servis {runId}`, tekan Enter
17. Verifikasi tidak ada baris untuk `Bengkel Mitra Teknik Servis {runId}`: tabel kosong dengan pesan `No results found`
18. Klik `Changelog` pada toolbar
19. Ketik Search `Bengkel Mitra Teknik Utama {runId}` pada modal `Changelog: Service Center`, tekan Enter
20. Verifikasi entri dengan Action `Updated`, Field `Name`, dan New Value `Bengkel Mitra Teknik Utama {runId}` tampil
21. Ganti isi kotak Search dengan `Bengkel Mitra Teknik Servis {runId}`, tekan Enter
22. Verifikasi tidak ada entri Changelog untuk `Bengkel Mitra Teknik Servis {runId}`: modal kosong dengan pesan `No results found`, karena simpan Admin A yang ditolak tidak dicatat
23. Tutup modal `Changelog: Service Center` lewat icon close

### Inactivate dengan versi usang ditolak dan tabel dimuat ulang dengan data terbaru
24. Ganti isi kotak Search dengan `Bengkel Rekanan Prima {runId}`, tekan Enter
25. Klik `⋯` pada baris `Bengkel Rekanan Prima {runId}`, lalu klik `Inactivate`
26. Admin B mengubah Name `Bengkel Rekanan Prima {runId}` menjadi `Bengkel Rekanan Prima Utama {runId}` lewat Edit dan menyimpannya
27. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
28. Verifikasi dialog `Service Center Changed` tampil
29. Verifikasi dialog memuat pesan `This service center was changed by someone else. Please review.`
30. Klik `[OK]`
31. Ganti isi kotak Search dengan `Bengkel Rekanan Prima Utama {runId}`, tekan Enter
32. Verifikasi baris `Bengkel Rekanan Prima Utama {runId}` tampil di tabel dengan nama terbaru dari Admin B
33. Verifikasi Status baris `Bengkel Rekanan Prima Utama {runId}` tetap `Active`, karena Inactivate Admin A yang ditolak tidak diterapkan
