---
id: TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action
title: "Detail: Tombol Aksi mengikuti Row Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-51
  - TC-AC-CS-585
  - TC-AC-CS-54
  - TC-AC-CS-55
coverage:
  web: automated
---

# Detail: Tombol Aksi mengikuti Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Group Manager scope Group `Jawa`, Distributor PT Maju Bersama; Pre-setup #5), password `Spectra.env.AC_SUB_GM_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #69 `SUBS-20250815-00001` (Warung Kopi Senja, FAMS Professional, Active, tanpa successor dan tanpa trial aktif), #60 `SUBS-20260810-00001` (PT Sejahtera, Trial Active), #54 `SUBS-20260201-00001` (Klinik Medika Jaya, Trial Expired), `SUBS-20260501-00001` (#66 Trial Converted), Client `PT Sejahtera` (#38) dengan tab Subscription, #57 `SUBS-20260819-00002` (Percetakan Mega, FAMS Professional, Pending; requester original `Dewi A`; Client berada di Group `Jawa` #35, sehingga masuk scope akun `Dewi Anggraini` #5).
- Dialog dan modal yang dibuka spec ditutup tanpa menyimpan (`✕` atau `[Go Back]`); spec tidak mengubah data.

## Test Steps

### TC-AC-CS-51: Tombol aksi Detail term Active mengikuti row action

1. Ketik Search `SUBS-20250815-00001`, tekan Enter
2. Klik baris `SUBS-20250815-00001`
3. Verifikasi tombol aksi: Renew, Cancel Subscription, Subscription Log
4. Verifikasi Edit, Cancel Request, dan Resubmit tidak ada
5. Verifikasi tombol berupa Button Outline dengan severity dark (Renew) dan danger (Cancel Subscription)

### TC-AC-CS-585: Tombol aksi Renew, Cancel Subscription, Edit, dan Cancel Request pada Detail berperilaku sama dengan row action (bagian Total Control Principal)

6. Klik tombol Renew pada card Subscription Info
7. Verifikasi modal "Renew Subscription" terbuka dengan Client `Warung Kopi Senja` dan Product `FAMS` Disabled dan terisi, sama dengan row action Renew
8. Klik `✕` pada modal
9. Klik tombol Cancel Subscription
10. Verifikasi dialog "Cancel Subscription" terbuka dengan bullet "• Warung Kopi Senja — FAMS — Professional", sama dengan row action
11. Klik `[Go Back]`
12. Verifikasi term `SUBS-20250815-00001` tetap Active

### TC-AC-CS-54: Tombol Convert pada Detail baris Trial Active dan Expired

13. Klik segmen `Client Subscription` pada Breadcrumb
14. Ganti isi kotak search dengan `SUBS-20260810-00001`, tekan Enter
15. Klik baris `SUBS-20260810-00001`
16. Verifikasi Detail Trial Active menampilkan tombol Convert
17. Klik tombol Convert
18. Verifikasi form `+ Subscription` varian Convert terbuka dengan judul "Convert Trial"
19. Klik `✕` pada form
20. Klik segmen `Client Subscription` pada Breadcrumb
21. Ganti isi kotak search dengan `SUBS-20260201-00001`, tekan Enter
22. Klik baris `SUBS-20260201-00001`
23. Verifikasi Detail Trial Expired menampilkan tombol Convert
24. Klik segmen `Client Subscription` pada Breadcrumb
25. Klik tab `History`
26. Ganti isi kotak search dengan `SUBS-20260501-00001`, tekan Enter
27. Klik baris `SUBS-20260501-00001`
28. Verifikasi Detail Trial Converted tidak menampilkan tombol Convert
29. Buka Client Detail `PT Sejahtera` lalu buka tab Subscription
30. Klik baris trial Active `SUBS-20260810-00001`
31. Verifikasi Subscription Detail yang dibuka dari Client Detail > Tab Subscription (read-only) tidak menampilkan tombol Convert

### TC-AC-CS-55: Detail yang dibuka dari Client Detail tab Subscription bersifat read-only

32. Kembali ke Client Detail `PT Sejahtera` pada tab Subscription
33. Klik baris term aktif `SUBS-20260101-00001`
34. Verifikasi Breadcrumb `Allocation > Client Subscription > Detail` tampil
35. Verifikasi tiga SectionCard tampil
36. Verifikasi seluruh tombol aksi (Renew, Edit, Cancel Subscription, Cancel Request, Resubmit, Convert, Subscription Log) tidak ada walau aktor Total Control

### TC-AC-CS-585: Tombol aksi Renew, Cancel Subscription, Edit, dan Cancel Request pada Detail berperilaku sama dengan row action (bagian Group Manager)

37. Logout lalu login sbg Role: Group Manager (Distributor, scoped) `Dewi Anggraini`
38. Buka menu `Allocation > Client Subscription`
39. Ketik Search `SUBS-20260819-00002`, tekan Enter
40. Klik baris `SUBS-20260819-00002`
41. Klik tombol Edit
42. Verifikasi modal "Edit Subscription" terbuka ter-isi dari record dengan Client, Product, Plan, dan Pay From Disabled
43. Klik `✕` pada modal
44. Klik tombol Cancel Request
45. Verifikasi dialog "Cancel Request" terbuka dengan bullet "• Percetakan Mega — FAMS" dan kalimat "You can resubmit it later if needed." karena aktor requester original
46. Klik `[Go Back]`
47. Verifikasi term `SUBS-20260819-00002` tetap Pending

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik segmen `Client Subscription` pada Breadcrumb, klik tab `History`, serta menutup modal lewat `✕`. Ganti akun punya langkah eksplisit (S-07).
- TC-AC-CS-585 ditulis dalam dua blok karena aktor berbeda; urutan TC: 51, 585 (Principal), 54, 55, 585 (Group Manager) supaya ganti akun hanya sekali (S-10). Rujukan TC-AC-CS-52 (Detail Waiting for Approval) ada di spec 008 dan TC-AC-CS-53 (Detail Canceled) di spec 009.
- Spec ini 47 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (tombol aksi pada Detail) pada data Pre-setup baca-saja, dan berdiri sendiri; TC-AC-CS-54 membuka lima Detail berbeda dan TC-AC-CS-585 memakai dua akun sehingga langkah Search, buka Detail, dan ganti akun tidak dapat dilebur.
- Temuan untuk QA:
  - TC-AC-CS-585 Expected a, c menyebut isian modal "ter-isi dari record" tanpa menyebut nilai Plan dan Pay From; spec mengasersi teks Expected tanpa menambah nilai.
  - TC-AC-CS-54 langkah 5 dan TC-AC-CS-55 sama-sama membuka Client Detail > tab Subscription lalu baris term aktif; keduanya tetap ditulis karena Expected d TC-AC-CS-54 mengasersi tombol Convert sedangkan TC-AC-CS-55 mengasersi seluruh tombol aksi.
  - TC-AC-CS-585 mengasersi "kedua term tetap Active dan Pending" setelah `[Go Back]`; spec memverifikasi per term setelah dialog masing-masing.
