---
id: TC-FA-FAREG-E2E-108-definisi-custom-field-berubah-dep-settings-custom-fields
title: "Definisi Custom field berubah: draft mengikuti definisi terbaru"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FAREG-LOGIC-08f]
smoke: []
dependsOn: ["Settings Custom Fields: definisi Custom field"]
trace:
  FAREG-LOGIC-08f: [5, 7, 15, 22, 29, 35, 36]
anchor: [13, 14, 21, 28]
coverage:
  web: automated
---

# Definisi Custom field berubah: draft mengikuti definisi terbaru

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Custom {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang memicu perubahan definisi Custom field.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-108-1: Group `Gudang Custom {runId}`, ada di entitas aktor.
  - DU-108-2: Asset Name `Server Custom {runId}` dengan TAG Type `Non-TAG`, Brand `Dell`, Model `PowerEdge R650`.
  - DU-108-3: Custom field Specific Asset Name `Nomor Rak {runId}` (Value Type Specific, opsional) dan `Lokasi Ruang {runId}` (Value Type Specific, opsional), serta `Kode Cabang {runId}` (Value Type Specific, opsional) untuk Asset Name `Server Custom {runId}`.
  - DU-108-4: batch Draft `Gudang Custom {runId}` berisi 1 Item Asset Name `Server Custom {runId}`, Brand `Dell`, Model `PowerEdge R650`, Quantity `1`, dengan `Nomor Rak {runId}` bernilai `RAK-108-01` dan `Kode Cabang {runId}` bernilai `CAB-108-02`.

## Test Steps

### Custom field wajib baru memblokir Activate
1. Admin menjadikan Custom field `Lokasi Ruang {runId}` wajib untuk Asset Name `Server Custom {runId}`
2. Ketik Search `Gudang Custom {runId}`, tekan Enter
3. Klik row action `Edit` pada baris batch `Gudang Custom {runId}`
4. Klik tab `Asset`
5. Verifikasi kolom `Lokasi Ruang {runId}` tampil dengan placeholder `Enter value`
6. Klik `[Submit]`
7. Verifikasi `Alert` Danger `Please complete the data for 1 asset to continue.` tampil di atas footer

### Custom field yang dihapus tidak lagi tampil
8. Admin menghapus Custom field `Nomor Rak {runId}`
9. Buka Fixed Asset > Assets > Registration > Draft
10. Ketik Search `Gudang Custom {runId}`, tekan Enter
11. Klik row action `Edit` pada baris batch `Gudang Custom {runId}`
12. Klik tab `Asset`
13. Verifikasi kolom `Condition` tampil
14. Verifikasi kolom `Lokasi Ruang {runId}` tampil
15. Verifikasi kolom `Nomor Rak {runId}` tidak tampil

### Nilai Custom field yang dihapus dibuang
16. Admin membuat ulang Custom field Specific `Nomor Rak {runId}` (Value Type Specific, opsional) untuk Asset Name `Server Custom {runId}`
17. Buka Fixed Asset > Assets > Registration > Draft
18. Ketik Search `Gudang Custom {runId}`, tekan Enter
19. Klik row action `Edit` pada baris batch `Gudang Custom {runId}`
20. Klik tab `Asset`
21. Verifikasi kolom `Nomor Rak {runId}` tampil
22. Verifikasi kolom `Nomor Rak {runId}` tidak berisi `RAK-108-01`, placeholder `Enter value` tampil

### Custom field yang bukan lagi Per asset tidak tampil sebagai kolom
23. Admin mengubah Custom field `Kode Cabang {runId}` menjadi bukan Per asset (Value Type bukan `Specific`)
24. Buka Fixed Asset > Assets > Registration > Draft
25. Ketik Search `Gudang Custom {runId}`, tekan Enter
26. Klik row action `Edit` pada baris batch `Gudang Custom {runId}`
27. Klik tab `Asset`
28. Verifikasi kolom `Lokasi Ruang {runId}` tampil
29. Verifikasi kolom `Kode Cabang {runId}` tidak tampil

### Nilai Custom field yang bukan lagi Per asset dibuang
30. Admin mengembalikan Custom field `Kode Cabang {runId}` menjadi Value Type `Specific`
31. Buka Fixed Asset > Assets > Registration > Draft
32. Ketik Search `Gudang Custom {runId}`, tekan Enter
33. Klik row action `Edit` pada baris batch `Gudang Custom {runId}`
34. Klik tab `Asset`
35. Verifikasi kolom `Kode Cabang {runId}` tampil
36. Verifikasi kolom `Kode Cabang {runId}` tidak berisi `CAB-108-02`, placeholder `Enter value` tampil
