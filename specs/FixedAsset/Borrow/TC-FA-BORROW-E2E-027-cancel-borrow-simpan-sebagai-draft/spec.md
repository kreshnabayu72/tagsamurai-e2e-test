---
id: TC-FA-BORROW-E2E-027-cancel-borrow-simpan-sebagai-draft
title: "Cancel Borrow dengan Save as Draft to edit membuat Draft baru berisi aset baris yang dibatalkan"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["F-BORROW-10.k8", "§9.2#p40", "§9.2#b80", "§9.2#b81", "§9.2#b82", "§9.2#b84", "§9.2#b85", "§9.2#b86", "§9.2#b87"]
smoke: []
dependsOn: []
trace:
  "F-BORROW-10.k8": [6, 7, 33]
  "§9.2#p40": [9, 24]
  "§9.2#b80": [9, 24]
  "§9.2#b81": 14
  "§9.2#b82": 25
  "§9.2#b84": 21
  "§9.2#b85": [40, 44, 47]
  "§9.2#b86": 11
  "§9.2#b87": [18, 23]
anchor: [32]
coverage:
  web: automated
---

# Cancel Borrow dengan Save as Draft to edit membuat Draft baru berisi aset baris yang dibatalkan

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`; ia bukan Borrower maupun PIC pada BRW di spec ini.
- Layar awal: halaman utama aplikasi dengan sidebar.
- Data:
  - DU-027-1: BRW Group `Head Office`, Borrower `Qori Fadillah {runId}`, Requested By `Agus Pratama {runId}`, Note `Untuk pelatihan Q4`, berisi baris aset DU-027-2 dan DU-027-3 berstatus `Waiting for Handover`; belum ada baris `Borrowed`.
  - DU-027-2: aset `Laptop MSI Modern {runId}`, Duration `3 days`, Purpose `Pelatihan karyawan`.
  - DU-027-3: aset `Proyektor Viewsonic {runId}`, Duration `2 days`, Purpose `Presentasi vendor`.
  - DU-027-4: BRW Group `Head Office`, Borrower `Rosa Anggraini {runId}`, berisi baris aset DU-027-5 berstatus `Borrowed` dan aset DU-027-6 berstatus `Waiting for Handover`.
  - DU-027-5: aset `Printer Brother {runId}`.
  - DU-027-6: aset `Scanner Fujitsu {runId}`, Duration `2 days`, Purpose `Pemindaian arsip`.
  - DU-027-7: BRW Group `Head Office`, Borrower `Sinta Wulandari {runId}`, Requested By `Agus Pratama {runId}`, Note `Peminjaman acara kantor`, berisi baris aset DU-027-8 berstatus `Waiting for Handover` yang batas pengambilannya (Transaction timeout) sudah terlewati saat job Transaction timeout berjalan.
  - DU-027-8: aset `Kamera Canon M50 {runId}`, Duration `4 days`, Purpose `Dokumentasi acara`.
  - Pada level plan Full, sehingga Draft tersedia.

## Test Steps

### Cancel Borrow dengan Save as Draft to edit
1. Klik `Transactions` pada sidebar
2. Klik `Borrow`
3. Ketik Search `Qori Fadillah {runId}`, tekan Enter
4. Klik menu ⋯ pada baris BRW milik DU-027-1
5. Klik `Cancel Borrow`
6. Verifikasi dialog `Cancel Borrow` memuat checkbox `Save as Draft to edit` yang tidak tercentang, karena BRW belum punya baris `Borrowed` dan Aktor ini Aktor Borrow dengan cakupan Group BRW
7. Verifikasi teks bantu `The assets become available again and the borrower and approvers are notified.` tampil selama checkbox tidak tercentang
8. Centang checkbox `Save as Draft to edit`
9. Verifikasi teks bantu berubah menjadi `The assets become available again and a new draft with the same details is created so you can fix and resubmit it.`
10. Klik `[Cancel Borrow]`
11. Verifikasi toast `Success, borrow has been canceled and saved as a draft.` tampil tanpa tautan

### BRW tetap tercatat Canceled dan Draft baru berisi aset baris yang dibatalkan
12. Klik tab `History`
13. Ketik Search `Qori Fadillah {runId}`, tekan Enter
14. Verifikasi baris BRW milik DU-027-1 tampil di tab `History` dengan status `Canceled`
15. Buka Borrow Detail BRW milik DU-027-1 dari tabel History
16. Klik menu ⋯ pada baris aset DU-027-2
17. Klik `Borrow Log`
18. Verifikasi node `Canceled by [Actor]` di Borrow Log aset DU-027-2 memuat baris detail `Saved as draft` berupa tautan ke Draft dengan [Actor] berisi `Agus Pratama {runId}`
19. Klik tab `Drafts`
20. Ketik Search `Qori Fadillah {runId}`, tekan Enter
21. Verifikasi Draft baru atas Borrower `Qori Fadillah {runId}` tampil tanpa nomor BRW dengan Modified By `Agus Pratama {runId}` sebagai pembuat Draft
22. Buka Draft atas Borrower `Qori Fadillah {runId}`
23. Verifikasi Draft menampilkan `Restored from [BRW No.]` dengan [BRW No.] berisi Transaction ID milik DU-027-1
24. Verifikasi Draft memuat aset DU-027-2 dengan Duration `3 days` dan Purpose `Pelatihan karyawan` serta aset DU-027-3 dengan Duration `2 days` dan Purpose `Presentasi vendor`
25. Verifikasi aset DU-027-2 dan DU-027-3 pada Draft tidak ditandai tidak layak, sehingga Custody keduanya sudah `Available` dan tidak dikunci Draft

### Checkbox Save as Draft to edit tidak tampil bila BRW sudah punya baris Borrowed
26. Klik `Transactions` pada sidebar
27. Klik `Borrow`
28. Ketik Search `Rosa Anggraini {runId}`, tekan Enter
29. Buka Borrow Detail BRW milik DU-027-4
30. Klik menu ⋯ pada baris aset DU-027-6
31. Klik `Cancel Borrow`
32. Verifikasi dialog `Cancel Borrow` menampilkan teks bantu `The assets become available again and the borrower and approvers are notified.`
33. Verifikasi checkbox `Save as Draft to edit` tidak tampil pada dialog karena BRW sudah punya baris `Borrowed`
34. Klik `[Go Back]`

### Penutupan otomatis oleh sistem menghasilkan bentuk yang sama tanpa dialog
35. Job Transaction timeout berjalan sesudah batas pengambilan baris DU-027-8 terlewati
36. Klik `Transactions` pada sidebar
37. Klik `Borrow`
38. Klik tab `History`
39. Ketik Search `Sinta Wulandari {runId}`, tekan Enter
40. Verifikasi baris BRW milik DU-027-7 tampil di tab `History` dengan status `Canceled` tanpa dialog konfirmasi
41. Buka Borrow Detail BRW milik DU-027-7 dari tabel History
42. Klik menu ⋯ pada baris aset DU-027-8
43. Klik `Borrow Log`
44. Verifikasi node `Canceled by System` di Borrow Log aset DU-027-8 dengan alasan `Not picked up` dan baris detail `Saved as draft`
45. Klik tab `Drafts`
46. Ketik Search `Sinta Wulandari {runId}`, tekan Enter
47. Verifikasi Draft baru atas Borrower `Sinta Wulandari {runId}` tampil dengan `Restored from [BRW No.]` dan aset DU-027-8 dengan Duration `4 days` dan Purpose `Dokumentasi acara`, tanpa nomor BRW
