---
id: TC-FA-SU-E2E-424-modal-assign-dan-popup-assign-group-transaction-role-target-ber-constraint-node-disabled-dan-tooltip-s-45
title: "Modal Assign Transaction Role dan Popup Assign Group Transaction Role Target Ber-constraint: Node Disabled dan Tooltip S-45"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1117
  - TC-FA-SU-1118
coverage:
  web: automated
---

# Modal Assign Transaction Role dan Popup Assign Group Transaction Role Target Ber-constraint: Node Disabled dan Tooltip S-45

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable; IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa dengan anak Jakarta Selatan Distribution Center) dan seed `FaUserHGT` (Pre-setup #51; varian `FaUserMain`, Home Group tidak dikosongkan). Seed `FaUserHGT` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Gita Permata (Pre-setup #51; Home Group Finance & Accounting; Transaction Role Disposal × Asset Admin pada Finance & Accounting, Disposal × Approver pada Accounts Payable, Damaged × Staff pada IT Infrastructure). Gita Permata juga akun aktor Pre-setup #20; di spec ini hanya menjadi pengguna target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: modal Assign dengan node dicentang Accounts Payable (langkah 19 sampai 20); popup Assign Group baris Disposal × Asset Admin (Finance & Accounting) dengan node dicentang Accounts Payable (langkah 35); node di luar constraint IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserHGT` (Pre-setup #51) di hook `before` dan sebagai pemulihan cadangan di hook `after`. Selektor node pohon, status Disabled, label tombol Group, dan tooltip disediakan tim FE.
- State global yang diubah: tidak ada data yang disimpan; modal dibuang lewat `[Leave]` dan popup lewat `[Cancel]`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, dan penugasan #51).

## Test Steps

### TC-FA-SU-1117: Modal Assign Transaction Role target ber-constraint: tree Group menonaktifkan node di luar constraint dengan tooltip S-45 dan node dalam constraint dapat dipilih

1. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Catat jumlah baris Sub-tab Transaction Role dan badge grup baris Disposal × Asset Admin sebagai baseline
4. Klik `[+ Assign]`, lalu klik tombol Group
5. Verifikasi Finance & Accounting (node constraint) tidak Disabled dan dapat dicentang
6. Verifikasi Accounts Payable (descendant) tidak Disabled dan dapat dicentang
7. Arahkan kursor ke IT Infrastructure
8. Verifikasi IT Infrastructure tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
9. Arahkan kursor ke Branch Surabaya
10. Verifikasi Branch Surabaya tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
11. Arahkan kursor ke General Affairs
12. Verifikasi General Affairs tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
13. Arahkan kursor ke Logistics Warehouse
14. Verifikasi Logistics Warehouse tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
15. Arahkan kursor ke Region Jawa
16. Verifikasi Region Jawa tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
17. Arahkan kursor ke Jakarta Selatan Distribution Center
18. Verifikasi Jakarta Selatan Distribution Center tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
19. Centang Accounts Payable
20. Klik `[Select]`
21. Verifikasi label tombol Group menjadi `1 Group selected`
22. Klik `[✕]` pada modal
23. Verifikasi dialog `Unsaved Changes`
24. Klik `[Leave]`
25. Verifikasi Sub-tab Transaction Role Gita Permata memuat jumlah baris dan badge baris Disposal × Asset Admin yang sama dengan baseline langkah 3 (tidak ada perubahan tersimpan)

### TC-FA-SU-1118: Popup Assign Group Transaction Role target ber-constraint: node di luar constraint Disabled dengan tooltip S-45, node dalam constraint dapat dipilih

26. Klik `[Assign Group]` pada baris Disposal × Asset Admin
27. Verifikasi Finance & Accounting tercentang (grup ter-assign) dan tidak Disabled
28. Verifikasi Accounts Payable tidak Disabled dan dapat dicentang
29. Arahkan kursor ke IT Infrastructure
30. Verifikasi IT Infrastructure tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
31. Arahkan kursor ke Branch Surabaya
32. Verifikasi Branch Surabaya tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
33. Arahkan kursor ke Region Jawa
34. Verifikasi Region Jawa tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
35. Centang Accounts Payable
36. Verifikasi `[Save]` Enabled
37. Klik `[Cancel]`
38. Verifikasi popup tertutup tanpa dialog `Unsaved Changes`
39. Verifikasi baris Disposal × Asset Admin memuat badge Finance & Accounting saja dan jumlah baris Sub-tab Transaction Role sama dengan baseline langkah 3 (tidak ada perubahan tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, dan 3. Search `Gita Permata` pada langkah 1 menemukan baris target (R-16, R-23). Baseline langkah 3 dipakai Expected d TC-FA-SU-1117 (langkah 25) dan Expected d TC-FA-SU-1118 (langkah 39).
- Verifikasi status node pada langkah 8, 10, 12, 14, 16, 18, 30, 32 dan 34 satu per node memuat tiga sifat yang dinyatakan TC dalam satu butir Expected b: Disabled, tidak dapat dicentang, dan tooltip (elemen "Disabled dengan tooltip", S-01). Hover mendahului tiap asersi tooltip (bagian 8b butir 5).
- Penutupan modal dirty pada langkah 22 sampai 24 mengikuti S-08; popup Assign Group ditutup lewat `[Cancel]` (langkah 37).
- Alasan di atas sekitar 35 langkah (39): dua TC memakai aktor, target, dan seed yang sama tanpa kelas harness dan tanpa perubahan data. Jumlah langkah dibentuk oleh Expected b yang dipecah satu `Verifikasi` per node di luar constraint (6 node pada TC-FA-SU-1117, 3 node pada TC-FA-SU-1118) beserta hover-nya (S-01, bagian 8b butir 5).
- TC-FA-SU-1117 dan TC-FA-SU-1118 hanya di spec ini. Pemilih lain dengan gate yang sama ada di spec 423, 425, dan 426.
- Temuan untuk QA:
  - Copy tooltip S-45 ("This group is outside the user's home group.") masih usulan (NC-27). Spec mengasersi literal TC; ubah bila PM mengganti copy.
  - Seed `FaUserHGT` (Pre-setup #51) wajib disediakan tim FE/BE; kunci fixture baru (node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, penugasan #51) dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - TC-FA-SU-1117 Expected d ("tidak ada perubahan tersimpan setelah modal ditutup") tidak menyebut cara observasi; spec mengasersinya lewat jumlah baris dan badge baris Disposal × Asset Admin terhadap baseline langkah 3.
  - TC-FA-SU-1117 langkah 6 menutup modal lewat `[Leave]` sehingga spec menuliskan `[✕]`, dialog `Unsaved Changes`, lalu `[Leave]` (S-08); modal dirty karena Accounts Payable sudah dipilih.
  - TC-FA-SU-1118 Expected c ("Setelah Accounts Payable dicentang `[Save]` Enabled") tidak menyebut state `[Save]` sebelum dicentang; spec mengasersi hanya state Enabled sesudah centang.
  - Post Condition kedua TC ("Tidak ada perubahan data") hanya diasersi lewat Expected d masing-masing.
