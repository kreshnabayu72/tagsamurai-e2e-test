---
id: TC-FA-FAREG-E2E-105-master-berubah-saat-draft-dep-settings-asset-name
title: "Master Asset Name, Brand, atau Model berubah: draft divalidasi ulang"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: [F-FAREG-03.k1, FAREG-LOGIC-08a, FAREG-LOGIC-08c, FAREG-LOGIC-08d, FAREG-LOGIC-08f, §9.4.2#r2, §9.7#r14, V-REG-04, S-REG-19]
smoke: [V-REG-04, S-REG-19]
dependsOn:
  - "Settings Asset Name: arsip, hapus, dan lepas Brand atau Model"
trace:
  F-FAREG-03.k1: [4, 5, 11]
  FAREG-LOGIC-08a: [4, 16, 23]
  FAREG-LOGIC-08c: [5, 6, 7, 17, 18, 24]
  FAREG-LOGIC-08d: [9, 11]
  FAREG-LOGIC-08f: [30, 31, 33]
  §9.4.2#r2: [5, 6, 7]
  §9.7#r14: [4, 16, 23]
  V-REG-04: [4, 16, 23]
  S-REG-19: 4
anchor: [30]
coverage:
  web: automated
---

# Master Asset Name, Brand, atau Model berubah: draft divalidasi ulang

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Master A {runId}`, `Gudang Master B {runId}`, `Gudang Master C {runId}`, dan `Gudang Master D {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu perubahan master.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-105-1: Group `Gudang Master A {runId}`, ada di entitas aktor.
  - DU-105-2: Group `Gudang Master B {runId}`, ada di entitas aktor.
  - DU-105-3: Group `Gudang Master C {runId}`, ada di entitas aktor.
  - DU-105-4: Group `Gudang Master D {runId}`, ada di entitas aktor.
  - DU-105-5: Asset Name `Laptop Master A {runId}` dengan TAG Type `RFID`, Brand `Dell`, dan Model `Latitude 5440`.
  - DU-105-6: Asset Name `Laptop Master B {runId}` dengan TAG Type `RFID`, Brand `Lenovo`, dan Model `ThinkPad T14`.
  - DU-105-7: Asset Name `Laptop Master C {runId}` dengan TAG Type `RFID`, Category `Komputer C {runId}`, Brand `Dell`, dan Model `Latitude 5440`.
  - DU-105-8: Asset Name `Laptop Master D {runId}` dengan TAG Type `RFID`, Brand `Dell`, dan Model `Latitude 5440`.
  - DU-105-9: batch Draft `Gudang Master A {runId}` berisi 1 Item Asset Name `Laptop Master A {runId}`, Brand `Dell`, Model `Latitude 5440`, Quantity `3`, dengan peringatan yang diharapkan `Dell is not available. Choose another Brand.`
  - DU-105-10: batch Draft `Gudang Master B {runId}` berisi 1 Item Asset Name `Laptop Master B {runId}`, Brand `Lenovo`, Model `ThinkPad T14`, Quantity `3`, dengan peringatan yang diharapkan `ThinkPad T14 is not available. Choose another Model.`
  - DU-105-11: batch Draft `Gudang Master C {runId}` berisi 1 Item Asset Name `Laptop Master C {runId}`, Brand `Dell`, Model `Latitude 5440`, Quantity `3`.
  - DU-105-12: batch Draft `Gudang Master D {runId}` berisi 1 Item Asset Name `Laptop Master D {runId}`, Brand `Dell`, Model `Latitude 5440`, Quantity `3`, dengan peringatan yang diharapkan `Laptop Master D {runId} is not available. Choose another Asset Name.`
  - DU-105-13: Category `Komputer Baru {runId}`, ada di master Category.

## Test Steps

### Brand dilepas dari Asset Name
1. Admin melepas Brand `Dell` dari Asset Name `Laptop Master A {runId}`
2. Ketik Search `Gudang Master A {runId}`, tekan Enter
3. Klik row action `Edit` pada baris batch `Gudang Master A {runId}`
4. Verifikasi `Alert` Warning `Dell is not available. Choose another Brand.` tampil di atas form
5. Verifikasi Brand dikosongkan: placeholder `Select brand` tampil
6. Verifikasi Model dikosongkan: placeholder `Select model` tampil
7. Verifikasi Quantity tetap `3`
8. Klik `[Save draft]`
9. Verifikasi toast `Success, draft has been saved.`
10. Klik `[Submit]`
11. Verifikasi `Alert` Danger `Please complete the data for 3 assets to continue.` tampil di atas footer

### Model diarsipkan
12. Admin mengarsipkan Model `ThinkPad T14` milik Brand `Lenovo` pada Asset Name `Laptop Master B {runId}`
13. Buka Fixed Asset > Assets > Registration > Draft
14. Ketik Search `Gudang Master B {runId}`, tekan Enter
15. Klik row action `Edit` pada baris batch `Gudang Master B {runId}`
16. Verifikasi `Alert` Warning `ThinkPad T14 is not available. Choose another Model.` tampil di atas form
17. Verifikasi Model dikosongkan: placeholder `Select model` tampil
18. Verifikasi Brand tetap `Lenovo`

### Asset Name diarsipkan
19. Admin mengarsipkan Asset Name `Laptop Master D {runId}`
20. Buka Fixed Asset > Assets > Registration > Draft
21. Ketik Search `Gudang Master D {runId}`, tekan Enter
22. Klik row action `Edit` pada baris batch `Gudang Master D {runId}`
23. Verifikasi `Alert` Warning `Laptop Master D {runId} is not available. Choose another Asset Name.` tampil di atas form

24. Verifikasi Asset Name dikosongkan: placeholder `Select asset name` tampil

### Category dan tipe Tag mengikuti Asset Name
25. Admin mengubah Category Asset Name `Laptop Master C {runId}` menjadi `Komputer Baru {runId}`
26. Admin mengubah TAG Type Asset Name `Laptop Master C {runId}` menjadi `QR`
27. Buka Fixed Asset > Assets > Registration > Draft
28. Ketik Search `Gudang Master C {runId}`, tekan Enter
29. Klik row action `Edit` pada baris batch `Gudang Master C {runId}`
30. Verifikasi Category Item `Komputer Baru {runId}` tampil
31. Verifikasi tidak ada `Alert` Warning di atas form
32. Klik tab `Asset`
33. Verifikasi tombol `Scan QR` tampil pada kolom TAG
