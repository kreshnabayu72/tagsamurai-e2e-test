---
id: TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record
title: "Penyuntingan Divisi Berhasil: Pengubahan Name, Code, Keduanya Sekaligus, Edit Record Seed, dan Refleksi Instan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-101
  - TC-GS-DIV-102
  - TC-GS-DIV-103
  - TC-GS-DIV-104
  - TC-GS-DIV-109
  - TC-GS-DIV-112
coverage:
  web: automated
---

# Penyuntingan Divisi Berhasil: Pengubahan Name, Code, Keduanya Sekaligus, Edit Record Seed, dan Refleksi Instan

## Prerequisites

- Login sebagai Role: Total Control
- Division "Treasury" (TRS) dan data seed ada di entitas
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)
- Division Pre-setup `Treasury` (Code `TRS`) ada

## Test Steps

### Edit hanya Division Name berhasil dan Code tidak berubah (TC-GS-DIV-101)

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Ubah Division Name menjadi `Accounting and Tax`
3. Klik `[Save]`
4. Muat ulang halaman (F5) dan lihat baris
5. Verifikasi Muncul toast sukses: `Success, division has been updated.`
6. Verifikasi Modal Edit tertutup
7. Verifikasi Setelah F5 baris menampilkan Name `Accounting and Tax` dan Code tetap `ACC`
8. Verifikasi Last Updated baris diperbarui

### Edit hanya Code berhasil dan Name tidak berubah (TC-GS-DIV-102)

9. Buka row action baris `Procurement` lalu klik `Edit`
10. Ubah Code menjadi `PROC`
11. Klik `[Save]`
12. Muat ulang halaman (F5) dan lihat baris
13. Verifikasi Muncul toast sukses: `Success, division has been updated.`
14. Verifikasi Setelah F5 baris menampilkan Code `PROC` dan Name tetap `Procurement`

### Edit Division Name dan Code sekaligus berhasil (TC-GS-DIV-103)

15. Buka row action baris `Production` lalu klik `Edit`
16. Ubah Division Name menjadi `Manufacturing` dan Code menjadi `MFG`
17. Klik `[Save]`
18. Verifikasi Muncul toast sukses: `Success, division has been updated.`
19. Verifikasi Tabel menampilkan Name `Manufacturing` dan Code `MFG`

### Division Pre-setup dapat di-Edit seperti Division lain (TC-GS-DIV-104)

20. Buka row action baris `Treasury` lalu klik `Edit`
21. Ubah Division Name menjadi `Treasury Management`
22. Klik `[Save]`
23. Verifikasi Modal Edit dapat dibuka dan Name dapat diubah
24. Verifikasi Muncul toast sukses: `Success, division has been updated.`

### Rename Division tercermin di Division Name pada tabel setelah Save (TC-GS-DIV-109)

25. Buka row action baris `Warehouse` lalu klik `Edit`
26. Ubah Division Name menjadi `Warehouse and Distribution`
27. Klik `[Save]`
28. Verifikasi Muncul toast sukses: `Success, division has been updated.`
29. Verifikasi Tabel langsung menampilkan `Warehouse and Distribution`

### Klik ganda Save hanya menyimpan satu kali (TC-GS-DIV-112)

30. Buka row action baris `Sales` lalu klik `Edit`
31. Ubah Division Name menjadi `Sales and Marketing`
32. Klik `[Save]` dua kali cepat
33. Verifikasi Tombol `[Save]` disabled setelah klik pertama
34. Verifikasi Hanya 1 perubahan tersimpan dan hanya 1 entri log Edit Name tercatat

## Notes

- Memvalidasi alur happy path Edit Name, Edit Code, mutasi seed record, toast sukses "Success, division has been updated.", dan refleksi seketika ke dropdown profil User (DIV-LOGIC-03, PRD §9.2, §9.7).
- Sumber pemetaan test case granular: TC-GS-DIV-101, TC-GS-DIV-102, TC-GS-DIV-103, TC-GS-DIV-104, TC-GS-DIV-109, TC-GS-DIV-112.
