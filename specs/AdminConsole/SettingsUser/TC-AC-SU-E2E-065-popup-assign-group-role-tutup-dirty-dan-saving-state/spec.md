---
id: TC-AC-SU-E2E-065-popup-assign-group-role-tutup-dirty-dan-saving-state
title: "Popup Assign Group Role: Tutup Bersih dan Dirty, serta Saving State Tombol Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-233
  - TC-AC-SU-234
  - TC-AC-SU-235
  - TC-AC-SU-232
coverage:
  web: automated
---

# Popup Assign Group Role: Tutup Bersih dan Dirty, serta Saving State Tombol Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE): `Budi Santoso {runId}-065` tanpa tingkat akses dan bukan Group Manager; `Manage partner` aktif di `Region A {runId}-065` (C ☐).
- Group Tree milik spec (seed lewat Fixture BE; setiap nama bersuffix `{runId}-065`): `Region A {runId}-065` > `Branch 1 {runId}-065` > `Floor 1 {runId}-065`; `Region A {runId}-065` > `Branch 3 {runId}-065`; `Region B {runId}-065`.
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-065@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-065`.
- Kemampuan teknis tambahan (TC-232): menahan respons request Save assignment lewat `Spectra.intercept` di atas backend nyata (throttle/hold response; menahan respons hanya untuk mengamati state Loading, bukan kelas b), melepas tahanan, dan membaca jumlah request Save yang terkirim; disediakan tim FE.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-065` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-233: Tutup Popup Assign Group Role bersih via ×

1. Ketik Search `Budi Santoso {runId}-065`, tekan Enter
2. Klik nama `Budi Santoso {runId}-065` di User List, Settings > User > Detail terbuka dengan Tab Role aktif
3. Klik Sub-tab [Group Role]
4. Klik `[Assign Group]` baris `Manage partner`
5. Klik `[×]`
6. Verifikasi popup langsung tertutup tanpa dialog Unsaved Changes

### TC-AC-SU-234: Tutup Popup Assign Group Role dirty via × lalu Cancel

7. Klik `[Assign Group]` baris `Manage partner`
8. Centang C baris `Region A {runId}-065`
9. Klik `[×]`
10. Verifikasi dialog dengan body `"You have unsaved changes. Are you sure you want to leave?"`, tombol `[Cancel]` `[Leave]`, tanpa bullet
11. Klik `[Cancel]` di dialog
12. Verifikasi dialog tertutup
13. Verifikasi popup tetap terbuka
14. Verifikasi C baris `Region A {runId}-065` tetap tercentang
15. Klik `✕` pada popup
16. Verifikasi dialog `"You have unsaved changes. Are you sure you want to leave?"` dengan tombol `[Cancel]` `[Leave]`
17. Klik `[Leave]`

### TC-AC-SU-235: Tutup Popup Assign Group Role dirty via Esc lalu Leave

18. Klik `[Assign Group]` baris `Manage partner`
19. Klik `[🗑]` baris `Region A {runId}-065`
20. Tekan Esc
21. Verifikasi dialog Unsaved Changes muncul
22. Klik `[Leave]`
23. Verifikasi popup tertutup
24. Verifikasi kolom Group `Manage partner` tetap `Region A {runId}-065`
25. Verifikasi tidak ada toast

### TC-AC-SU-232: Saving state tombol Save saat request berjalan

26. Tunggu toast lama hilang otomatis
27. Klik `[Assign Group]` baris `Manage partner`
28. Centang C baris `Region A {runId}-065`
29. Tahan respons request Save assignment (intercept)
30. Klik `[Save]`
31. Verifikasi `[Save]` menampilkan loading dan disabled
32. Verifikasi `[Clear Field]`, checkbox, dan `[×]` ikut disabled
33. Klik `[Save]` lagi selama loading
34. Verifikasi klik kedua tidak mengirim request baru (jumlah request Save tetap satu)
35. Lepas tahanan respons
36. Verifikasi hanya 1 toast sukses `"Success, group role has been updated."`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 26, 29, 35 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 233, 234, 235, 232. TC-232 menyimpan perubahan (C tercentang tersimpan) sehingga ditaruh terakhir agar TC-234 tidak bergantung pada nilai C yang sudah berubah.
- Menahan respons TC-232 hanya untuk mengamati state Loading dan bukan kelas b (bagian 3 prinsip 13); intercept dilepas segera setelah asersi (S-09).
- Pembagian TC: TC-AC-SU-236, 237, 241 ada di spec 066; TC-AC-SU-238, 239, 240 ada di spec 067.
- Temuan untuk QA:
  - Post Condition TC-232 ("Tepat 1 entri log Edit") tidak punya langkah observasi dan tidak diasersi.
  - Dialog Unsaved Changes pada TC-234 diasersi menurut Expected TC (body dan tombol); S-08 dipenuhi oleh urutan `✕`, `Verifikasi` dialog, `[Leave]`.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada permukaan dan kelas harness yang sama dan berdiri sendiri (target user milik spec per TC); kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian langkah hanya penghubung (pencarian target dan kembali ke User List).
