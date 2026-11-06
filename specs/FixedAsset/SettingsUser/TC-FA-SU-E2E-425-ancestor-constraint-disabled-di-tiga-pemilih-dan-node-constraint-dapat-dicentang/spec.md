---
id: TC-FA-SU-E2E-425-ancestor-constraint-disabled-di-tiga-pemilih-dan-node-constraint-dapat-dicentang
title: "Ancestor Constraint Disabled di Tiga Pemilih dan Node Constraint Dapat Dicentang"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1124
coverage:
  web: automated
---

# Ancestor Constraint Disabled di Tiga Pemilih dan Node Constraint Dapat Dicentang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Region Jawa dengan anak Jakarta Selatan Distribution Center) dan seed `FaUserHGT` (Pre-setup #51; varian `FaUserMain`, Home Group tidak dikosongkan). Seed `FaUserHGT` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Vina Maharani (Pre-setup #51; Home Group Jakarta Selatan Distribution Center, parent Region Jawa seperti Pre-setup #46; Transaction Role Transfer × Monitoring & Report pada Jakarta Selatan Distribution Center).
- Data uji: ancestor constraint Region Jawa; node constraint Jakarta Selatan Distribution Center; pemilih Select Group (baris Manage files), modal Assign Transaction Role (tombol Group), dan popup Assign Group Transaction Role (baris Transfer × Monitoring & Report).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserHGT` (Pre-setup #51) di hook `before` dan sebagai pemulihan cadangan di hook `after`. Selektor node pohon, status Disabled, status tercentang, dan tooltip disediakan tim FE.
- State global yang diubah: tidak ada data yang disimpan; popup dan modal dibuang lewat `[Cancel]` dan `[Leave]`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: node Region Jawa, Jakarta Selatan Distribution Center, dan penugasan #51).

## Test Steps

### TC-FA-SU-1124: Ancestor Home Group constraint Disabled di tiga pemilih: Select Group Group Role, modal Assign Transaction Role, dan popup Assign Group Transaction Role

1. Ketik Search `Vina Maharani`, tekan Enter, lalu klik Name `Vina Maharani`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Catat jumlah baris Sub-tab Transaction Role dan badge baris Transfer × Monitoring & Report sebagai baseline
4. Klik Sub-tab Group Role
5. Catat badge setiap baris Sub-tab Group Role sebagai baseline
6. Klik `[Assign Group]` pada baris Manage files, lalu klik `[+ Assign Group]`
7. Arahkan kursor ke Region Jawa
8. Verifikasi pada popup Select Group Region Jawa (ancestor constraint) tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
9. Verifikasi pada popup Select Group Jakarta Selatan Distribution Center (node constraint) tidak Disabled dan dapat dicentang
10. Centang Jakarta Selatan Distribution Center
11. Verifikasi Region Jawa tetap tidak tercentang dan tidak ada node lain yang tercentang selain Jakarta Selatan Distribution Center (tidak ada cascade ke ancestor atau descendant)
12. Klik `[Cancel]` pada popup Select Group, lalu klik `[Cancel]` pada popup Assign Group Role
13. Verifikasi Sub-tab Group Role Vina Maharani memuat badge setiap baris yang sama dengan baseline langkah 5 (tidak ada perubahan tersimpan)
14. Klik Sub-tab Transaction Role, klik `[+ Assign]`, lalu klik tombol Group
15. Arahkan kursor ke Region Jawa
16. Verifikasi pada modal Assign Transaction Role Region Jawa (ancestor constraint) tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
17. Verifikasi pada modal Assign Transaction Role Jakarta Selatan Distribution Center (node constraint) tidak Disabled dan dapat dicentang
18. Centang Jakarta Selatan Distribution Center
19. Verifikasi Region Jawa tetap tidak tercentang dan tidak ada node lain yang tercentang selain Jakarta Selatan Distribution Center (tidak ada cascade ke ancestor atau descendant)
20. Klik `[✕]` pada modal
21. Verifikasi dialog `Unsaved Changes`
22. Klik `[Leave]`
23. Klik `[Assign Group]` pada baris Transfer × Monitoring & Report
24. Arahkan kursor ke Region Jawa
25. Verifikasi pada popup Assign Group Transaction Role Region Jawa (ancestor constraint) tampil Disabled, tidak dapat dicentang, dan tooltip "This group is outside the user's home group." tampil
26. Verifikasi pada popup Assign Group Transaction Role Jakarta Selatan Distribution Center (node constraint) tidak Disabled dan tercentang
27. Klik `[Cancel]`
28. Verifikasi Sub-tab Transaction Role Vina Maharani memuat jumlah baris dan badge baris Transfer × Monitoring & Report yang sama dengan baseline langkah 3 (tidak ada perubahan tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 4, 5, dan 12. Search `Vina Maharani` pada langkah 1 menemukan baris target (R-16, R-23). Baseline langkah 3 dan 5 dipakai Expected d (langkah 13 dan 28).
- Expected a TC-FA-SU-1124 (Region Jawa Disabled, tidak dapat dicentang, tooltip) dan Expected b (Jakarta Selatan Distribution Center tidak Disabled, dapat dicentang, atau tercentang pada popup Assign Group) ditulis satu `Verifikasi` per pemilih (langkah 8, 9, 16, 17, 25, 26); Verifikasi Region Jawa memuat tiga sifat dalam satu butir Expected ("Disabled dengan tooltip", S-01). Hover mendahului tiap asersi tooltip (bagian 8b butir 5).
- Penutupan modal dirty pada langkah 20 sampai 22 mengikuti S-08; popup ditutup lewat `[Cancel]` (langkah 12, 27).
- Pembagian TC lintas spec: tidak ada; TC-FA-SU-1124 hanya di spec ini.
- Temuan untuk QA:
  - Copy tooltip S-45 ("This group is outside the user's home group.") masih usulan (NC-27). Spec mengasersi literal TC; ubah bila PM mengganti copy.
  - Seed `FaUserHGT` (Pre-setup #51) wajib disediakan tim FE/BE; kunci fixture baru (node Region Jawa, Jakarta Selatan Distribution Center, penugasan #51) dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - TC-FA-SU-1124 Expected c ("mencentang node tidak men-cascade ke ancestor atau descendant") tidak menyebut pemilih tempat observasi; spec mengasersinya pada popup Select Group dan modal Assign Transaction Role setelah Jakarta Selatan Distribution Center dicentang (langkah 11 dan 19). Pada popup Assign Group Transaction Role node itu sudah tercentang sejak dibuka sehingga tidak ada pencentangan yang diasersi. Descendant Jakarta Selatan Distribution Center tidak disebut Pre-setup #21; asersi mencakup "tidak ada node lain yang tercentang".
  - TC-FA-SU-1124 langkah 4 menutup modal lewat `[Leave]` sehingga spec menuliskan `[✕]`, dialog `Unsaved Changes`, lalu `[Leave]` (S-08); modal dirty karena Jakarta Selatan Distribution Center sudah dicentang.
  - TC-FA-SU-1124 Expected d ("tidak ada perubahan tersimpan") tidak menyebut cara observasi; spec membandingkan badge baris Sub-tab Group Role dan Sub-tab Transaction Role terhadap baseline langkah 3 dan 5.
  - Vina Maharani memiliki Group Role baris Manage files yang dibuka TC; isi awal baris Group Role Vina Maharani tidak disebut Pre-setup #51 sehingga baseline dicatat pada langkah 5.
