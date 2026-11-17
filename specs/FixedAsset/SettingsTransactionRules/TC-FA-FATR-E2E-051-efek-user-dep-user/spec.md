---
id: TC-FA-FATR-E2E-051-efek-user-dep-user
title: "Created By dan Modified By bertahan sesudah user berubah"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r283", "§4.1#r284", "§4.1#r285", "§4.1#r431", "§4.1#r432", "§4.1#r433", "§4.1#r430"]
smoke: []
dependsOn:
  - "Settings User: nonaktifkan, hapus, dan ubah nama user"
trace:
  "§4.1#r283": [23, 24, 33]
  "§4.1#r284": [32, 33]
  "§4.1#r285": 35
  "§4.1#r431": 26
  "§4.1#r432": [37, 38]
  "§4.1#r433": 40
  "§4.1#r430": [37, 38, 40]
anchor: []
coverage:
  web: automated
---

# Created By dan Modified By bertahan sesudah user berubah

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update) dan akses penuh ke Settings User; `Rina{runId} Susanti` sebagai Default User yang memegang Manage transaction settings (Update) dengan cakupan Group `Depot Bogor {runId}`, dan `Tono{runId} Wibowo` sebagai Default User yang memegang Manage transaction settings (Update) dengan cakupan Group `Depot Cirebon {runId}`; keduanya pembuat override dan pengubah setting.
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-051-1: Category Name `Cooling Equipment {runId}`; Category leaf tempat override dibuat.
  - DU-051-2: Group Name `Depot Bogor {runId}`; Group target override pertama.
  - DU-051-3: Group Name `Depot Cirebon {runId}`; Group target override kedua.
  - DU-051-4: User Name `Rina{runId} Susanti`, Role `Default User`, Manage transaction settings `Update`, cakupan Group `Depot Bogor {runId}`; pengguna yang akan dinonaktifkan sesudah membuat override dan menyimpan perubahan.
  - DU-051-5: User Name `Tono{runId} Wibowo`, Role `Default User`, Manage transaction settings `Update`, cakupan Group `Depot Cirebon {runId}`, Nama baru `Toni{runId} Wibowo`; pengguna yang akan diubah namanya lalu dihapus sesudah membuat override dan menyimpan perubahan.
- Kondisi:
  - Akun `Rina{runId} Susanti` dan `Tono{runId} Wibowo` aktif dan kredensialnya tersedia untuk login.

## Test Steps
### Created By dan Modified By mencatat nama pengaju apa adanya
1. Masuk sebagai `Rina{runId} Susanti`
2. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
3. Klik `[+ Override]` pada bagian Overrides
4. Isi Scope `Group` dengan Target `Depot Bogor {runId}`
5. Pilih Field `Max duration` dengan Value `15`
6. Klik `[Submit]`
7. Klik `[Set own value]` pada field Max duration
8. Isi Max duration dengan `16`
9. Klik `[Save]`
10. Klik `[Save]` pada dialog Save Changes
11. Masuk sebagai `Tono{runId} Wibowo`
12. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
13. Klik `[+ Override]` pada bagian Overrides
14. Isi Scope `Group` dengan Target `Depot Cirebon {runId}`
15. Pilih Field `Max duration` dengan Value `9`
16. Klik `[Submit]`
17. Klik `[Set own value]` pada field Max extensions
18. Isi Max extensions dengan `2`
19. Klik `[Save]`
20. Klik `[Save]` pada dialog Save Changes
21. Masuk sebagai Default User
22. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
23. Verifikasi kolom Created By baris override untuk `Depot Bogor {runId}` menampilkan nama depan utuh dan inisial nama belakang `Rina{runId} S` dari user `Rina{runId} Susanti`[^drift-1]
24. Verifikasi nama lengkap `Rina{runId} Susanti` tersampaikan saat hover pada Created By baris override untuk `Depot Bogor {runId}`
25. Buka dialog Changelog dari header halaman Transaction Settings
26. Verifikasi kolom Modified By entri perubahan Category `Cooling Equipment {runId}` dengan Field `Borrow (Max duration)` memuat nama depan utuh dan inisial nama belakang `Rina{runId} S` dari user `Rina{runId} Susanti`[^drift-1]
27. Tutup dialog Changelog

### Pembuat dan pengubah tetap tampil sesudah dinonaktifkan, diubah namanya, atau dihapus
28. Nonaktifkan user `Rina{runId} Susanti`
29. Ubah nama user `Tono{runId} Wibowo` menjadi `Toni{runId} Wibowo`
30. Hapus user `Toni{runId} Wibowo`
31. Buka tab `Borrow` pada node Category `Cooling Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
32. Verifikasi kolom Created By baris override untuk `Depot Bogor {runId}` tetap menampilkan `Rina{runId} S` sesudah user `Rina{runId} Susanti` dinonaktifkan[^drift-1]
33. Verifikasi kolom Created By baris override untuk `Depot Cirebon {runId}` tetap menampilkan `Tono{runId} W`, bukan `Toni{runId} W`, sesudah user diubah namanya dan dihapus[^drift-1]
34. Buka pilihan Created By pada Filter Panel tabel Overrides
35. Verifikasi opsi `All users` memuat nama pembuat `Rina{runId} Susanti` yang nonaktif dan `Tono{runId} Wibowo` yang terhapus
36. Buka dialog Changelog dari header halaman Transaction Settings
37. Verifikasi kolom Modified By entri perubahan Category `Cooling Equipment {runId}` dengan Field `Borrow (Max duration)` di Changelog tetap menampilkan `Rina{runId} S` sesudah user `Rina{runId} Susanti` dinonaktifkan[^drift-1]
38. Verifikasi kolom Modified By entri perubahan Category `Cooling Equipment {runId}` dengan Field `Borrow (Max extensions)` di Changelog tetap menampilkan `Tono{runId} W` sesudah user diubah namanya dan dihapus[^drift-1]
39. Buka pilihan Modified By pada Filter Panel Changelog
40. Verifikasi opsi `All users` memuat nama pengubah `Rina{runId} Susanti` yang nonaktif dan `Tono{runId} Wibowo` yang terhapus

[^drift-1]: Drift PRD vs foundation. PRD §4.1 `OVR-COL-CRT-a` dan `CHG-COL-MOD-a`: nama pembuat atau pengubah «ditulis apa adanya sebagai snapshot» saat baris dibuat atau entri dicatat. foundation `prd-conventions.md` §9.13 konteks 2: kolom referensi user sekunder ditampilkan sebagai Plain Text `[First Name] [Last Initial]`, dengan hover tooltip nama lengkap. Diasersi: foundation untuk bentuk tampilan nama (pola bersama, SB-4), dan «apa adanya» PRD diasersi sebagai snapshot: nama tidak ikut berubah sesudah user diubah namanya, dinonaktifkan, atau dihapus.
